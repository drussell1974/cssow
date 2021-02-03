# -*- coding: utf-8 -*-
import sys
from django.db import models
from enum import Enum
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

class TeacherPermissionModel(BaseModel):
    
    class Meta:
        permissions = [('can_manage_team_permissions','Can Manage Team Permissions')]

    def __init__(self, teacher_id, teacher_name, scheme_of_work, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE, department_permission=DEPARTMENT.NONE, created=None, auth_user=None, created_by_name=None, published=None, is_from_db=False, is_authorised = False):
        
        super().__init__(teacher_id, teacher_name, created=created, created_by_id=auth_user, created_by_name=created_by_name, published=published, is_from_db=is_from_db)

        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.scheme_of_work = scheme_of_work
        self.scheme_of_work_permission = scheme_of_work_permission
        self.lesson_permission = lesson_permission
        self.department_permission = department_permission
        self.is_authorised = is_authorised
        self.published = published
        self.is_from_db = is_from_db
        self.is_valid = False


    def is_new(self):
        return (self.is_from_db == False)
        

    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """       
        # TODO: #316 - clean auth_user_name
        if type(self.department_permission) is str:
            self.department_permission = DEPARTMENT[self.department_permission]
        if type(self.scheme_of_work_permission) is str:
            self.scheme_of_work_permission = SCHEMEOFWORK[self.scheme_of_work_permission]
        if type(self.lesson_permission) is str:
            self.lesson_permission = LESSON[self.lesson_permission]


    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)
        # teacher id
        self._validate_required_integer("teacher_id", self.teacher_id, 1, self.MAX_INT)
        # teacher name
        self._validate_required_string("teacher_name", self.teacher_name, 1, 150)
        # validate required department_permission
        self._validate_enum("department_permission", self.department_permission, DEPARTMENT)
        # validate required scheme_of_work_permission
        self._validate_enum("scheme_of_work_permission", self.scheme_of_work_permission, SCHEMEOFWORK)
        # validate required lesson_permission
        self._validate_enum("lesson_permission", self.lesson_permission, LESSON)
        
        return self.is_valid


    def check_permission(self, permission):
        if type(permission) == SCHEMEOFWORK:
            return self._check_scheme_of_work_permission(permission)
        elif type(permission) == LESSON:
            return self._check_lesson_permission(permission)
        elif type(permission) == DEPARTMENT:
            return self._check_department_permission(permission)
        else:
            raise TypeError("permission is type {}. Must be type DEPARTMENT or SCHEME_OF_WORK or LESSON.".format(type(permission)))


    def _check_scheme_of_work_permission(self, permission):
        return self.scheme_of_work_permission % permission == 0 and self.is_authorised == True


    def _check_lesson_permission(self, permission):
        return self.lesson_permission % permission == 0 and self.is_authorised == True


    def _check_department_permission(self, permission):
        return self.department_permission % permission == 0 and self.is_authorised == True


    @staticmethod
    def get_model(db, scheme_of_work, teacher_id, auth_user):
        ''' get permission for the teacher '''
        rows = TeacherPermissionDataAccess.get_model(db, scheme_of_work.id, teacher_id, auth_user)

        model = TeacherPermissionModel(teacher_id=teacher_id, teacher_name="", scheme_of_work=scheme_of_work) # Default
        model.is_from_db = False
        model.is_authorised = False
        
        for row in rows:
            model = TeacherPermissionModel(teacher_id=teacher_id, teacher_name=row[3], scheme_of_work=scheme_of_work, scheme_of_work_permission=row[0], lesson_permission=row[1], department_permission=row[2], is_from_db=True, is_authorised=row[4])
            return model
        return model


    @staticmethod
    def get_team_permissions(db, teacher_id, auth_user):

        cur_scheme_of_work = SchemeOfWorkModel(0)

        rows = TeacherPermissionDataAccess.get_team_permissions(db, teacher_id, auth_user)
        data = []
        for row in rows:
            
            # check for changed scheme of work
            if cur_scheme_of_work.id != row[2]:
                cur_scheme_of_work = SchemeOfWorkModel(row[2], name=row[3])
                data.append(cur_scheme_of_work)


            model = TeacherPermissionModel(
                teacher_id=row[0],
                teacher_name=row[1],
                scheme_of_work=cur_scheme_of_work,
                department_permission=DEPARTMENT(row[4]),
                scheme_of_work_permission=SCHEMEOFWORK(row[5]),
                lesson_permission=LESSON(row[6]),
                is_authorised=row[7],
                is_from_db = True
            )

            cur_scheme_of_work.teacher_permissions.append(model)

        return data


    @staticmethod
    def request_access(db, model, auth_user):
        if model.is_valid:
            TeacherPermissionDataAccess.insert_department__has__teacher(db, model, auth_user)
            data = TeacherPermissionDataAccess.insert_access_request(db, model, auth_user)
            return data
        return None


    @staticmethod
    def save(db, model, auth_user):
        """ save model """
        if model.is_new() == False and model.published == 2:
            data = TeacherPermissionDataAccess._delete(db, model.scheme_of_work.id, model.teacher_id, auth_user)
        elif model.is_valid == True:
            if model.is_new() == True:
                data = TeacherPermissionDataAccess._insert(db, model, auth_user)
                model.id = data[0]
            else:
                data = TeacherPermissionDataAccess._update(db, model, auth_user)
    
        return model

    @staticmethod
    def delete(db, model, auth_user):
        TeacherPermissionDataAccess._delete(db, model.scheme_of_work.id, model.teacher_id, auth_user)
        model.is_from_db = False
        return model


class TeacherPermissionDataAccess:

    @staticmethod
    def get_model(db, scheme_of_work_id, teacher_id, auth_user):
        ''' gets the current users permissions for the scheme of work  '''

        helper = ExecHelper()

        str_select = "scheme_of_work__get_teacher_permissions"
        params = (scheme_of_work_id, teacher_id, auth_user)
        
        rows = []
        rows = helper.select(db, str_select, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_team_permissions(db, head_id, auth_user):
        ''' gets the team permission for the current user '''

        execHelper = ExecHelper()

        str_select = "scheme_of_work__get_team_permissions"
        params = (head_id, auth_user)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting departments", e)


    @staticmethod
    def _insert(db, model, auth_user):
        """ inserts the sow_scheme_of_work__has__teacher """
    
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert"
        params = (
            model.scheme_of_work.id,
            model.teacher_id,
            DEPARTMENT(model.department_permission).value,
            SCHEMEOFWORK(model.scheme_of_work_permission).value,
            LESSON(model.lesson_permission).value,
            auth_user,
            model.is_authorised
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, auth_user):
        """ updates the sow_scheme_of_work__has__teacher """

        execHelper = ExecHelper()
        
        str_update = "scheme_of_work__has__teacher_permission__update"
        params = (
            model.scheme_of_work.id,
            model.teacher_id,
            DEPARTMENT(model.department_permission).value,
            SCHEMEOFWORK(model.scheme_of_work_permission).value,
            LESSON(model.lesson_permission).value,
            auth_user,
            model.is_authorised
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, scheme_of_work_id, teacher_id, auth_user):
        ''' deletes from sow_scheme_of_work__has__teacher''' 

        execHelper = ExecHelper()

        sql = "scheme_of_work__has__teacher_permission__delete"
        params = (scheme_of_work_id, teacher_id, auth_user)
    
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def insert_access_request(db, model, auth_user):
        """ inserts the sow_scheme_of_work__has__teacher """
    
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert"
        params = (
            model.scheme_of_work.id,
            model.teacher_id,
            DEPARTMENT(model.department_permission).value,
            SCHEMEOFWORK(model.scheme_of_work_permission).value,
            LESSON(model.lesson_permission).value,
            auth_user,
            model.is_authorised
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result

    
    @staticmethod
    def insert_department__has__teacher(db, model, auth_user):
        """ inserts the sow_department__has__teacher """
    
        execHelper = ExecHelper()

        sql_insert_statement = "department__has__teacher__insert"
        params = (
            model.teacher_id,
            model.scheme_of_work.department_id,
            DEPARTMENT(model.department_permission).value,
            SCHEMEOFWORK(model.scheme_of_work_permission).value,
            LESSON(model.lesson_permission).value,
            auth_user,
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result