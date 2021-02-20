# -*- coding: utf-8 -*-
import sys
from django.db import models
from enum import Enum
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.context import AuthCtx
from shared.models.core.basemodel import BaseModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

class TeacherPermissionModel(BaseModel):
    
    class Meta:
        permissions = [('can_manage_team_permissions','Can Manage Team Permissions')]


    @staticmethod
    def empty(institute_id, department_id, scheme_of_work_id, ctx):
        scheme_of_work = SchemeOfWorkModel.empty(ctx=ctx)
        
        return TeacherPermissionModel(teacher_id=ctx.auth_user_id, teacher_name="Anonymous", scheme_of_work=scheme_of_work, ctx=ctx) # Default


    def __init__(self, teacher_id, teacher_name, scheme_of_work, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE, department_permission=DEPARTMENT.NONE, created=None, auth_user=None, created_by_name=None, published=None, is_from_db=False, is_authorised = False, ctx = None):
        
        #329 Ensure ctx contains institute_id and department_id
        if ctx is None:
            raise KeyError(f"ctx cannot be {ctx}")
        
        super().__init__(teacher_id, teacher_name, created=created, created_by_id=auth_user, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=auth_user)
        
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.scheme_of_work_id = scheme_of_work.id
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

        # validate required name
        self._validate_required_string("teacher_name", self.teacher_name, 1, 70)
        # validate required department_permission
        self._validate_enum("department_permission", self.department_permission, DEPARTMENT)
        # validate required scheme_of_work_permission
        self._validate_enum("scheme_of_work_permission", self.scheme_of_work_permission, SCHEMEOFWORK)
        # validate required lesson_permission
        self._validate_enum("lesson_permission", self.lesson_permission, LESSON)
        
        self.on_after_validate()
        
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
    def get_model(db, teacher_id, scheme_of_work, auth_user, show_authorised=True, trace=False):
        ''' get permission for the teacher '''
        
        rows = TeacherPermissionDataAccess.get_model(db, scheme_of_work.id, teacher_id, auth_user.department_id, auth_user.institute_id, show_authorised=show_authorised, auth_user_id=auth_user.auth_user_id)
        
        model = TeacherPermissionModel.empty(scheme_of_work.institute_id, scheme_of_work.department_id, scheme_of_work.id, auth_user) # Default
        
        # NOTE: default valid if scheme of work is 0
        model.department_permission = DEPARTMENT.ADMIN if scheme_of_work.id == 0 else DEPARTMENT.NONE
        model.scheme_of_work_permission = SCHEMEOFWORK.OWNER if scheme_of_work.id == 0 else SCHEMEOFWORK.NONE
        model.lesson_permission = LESSON.OWNER if scheme_of_work.id == 0 else LESSON.NONE
        model.is_from_db = (scheme_of_work.id == 0)
        model.is_authorised = (scheme_of_work.id == 0)
        
        for row in rows:
            # returns only the matching row
            # TODO: Cache
            if auth_user.scheme_of_work_id == int(row[2]) and auth_user.department_id == int(row[4]) and auth_user.institute_id == int(row[6]):
                model = TeacherPermissionModel(teacher_id=teacher_id, teacher_name=row[3], scheme_of_work=scheme_of_work,  scheme_of_work_permission=row[8], lesson_permission=row[9], department_permission=row[10], is_from_db=True, is_authorised=bool(row[11]), ctx=auth_user)
                return model
        return model


    @staticmethod
    def get_team_permissions(db, teacher_id, auth_user, show_authorised=True):

        cur_scheme_of_work = SchemeOfWorkModel(0, auth_user=auth_user)

        rows = TeacherPermissionDataAccess.get_team_permissions(db, teacher_id, show_authorised=show_authorised, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            
            # check for changed scheme of work
            if cur_scheme_of_work.id != row[2]:
                cur_scheme_of_work = SchemeOfWorkModel(row[2], name=row[3], auth_user=auth_user)
                data.append(cur_scheme_of_work)

            #329 TODO: get by teacher_id only #create TeacherModel
            
            # TeacherModel(row[0], name=row[1], department=DepartmentModel(0,name=""))

            model = TeacherPermissionModel(
                teacher_id=row[0],
                teacher_name=row[1], #319 get teacher name
                scheme_of_work=cur_scheme_of_work,
                department_permission=DEPARTMENT(row[6]),
                scheme_of_work_permission=SCHEMEOFWORK(row[7]),
                lesson_permission=LESSON(row[8]),
                is_authorised=row[9],
                is_from_db = True,
                ctx = auth_user
            )

            cur_scheme_of_work.teacher_permissions.append(model)

        return data


    @staticmethod
    def request_access(db, model, auth_user):
        
        if model.is_valid:
            TeacherPermissionDataAccess.insert_department__has__teacher(db, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, ctx=auth_user)
            data = TeacherPermissionDataAccess.insert_access_request(db, model.scheme_of_work_id, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, auth_user)
            return data
        return None


    @staticmethod
    def save(db, model, auth_user, is_pending = False):
        """ save model """
        if model.is_new() == False and model.published == 2:
            data = TeacherPermissionDataAccess._delete(db, model.scheme_of_work_id, model.teacher_id, ctx=auth_user)
        elif model.is_valid == True:
            if model.is_new() == True:
                data = TeacherPermissionDataAccess._insert(db, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, ctx=auth_user)
                model.id = data[0]
            else:
                data = TeacherPermissionDataAccess._update(db, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, ctx=auth_user)
    
        return model


    @staticmethod
    def delete(db, model, auth_user):
        TeacherPermissionDataAccess._delete(db, model.scheme_of_work_id, model.teacher_id, ctx=auth_user)
        model.is_from_db = False
        return model


class TeacherPermissionDataAccess:

    @staticmethod
    def get_model(db, scheme_of_work_id, teacher_id, department_id, institute_id, show_authorised, auth_user_id):
        ''' gets the current users permissions for the scheme of work  '''
        
        helper = ExecHelper()

        str_select = "scheme_of_work__get_teacher_permissions"
        params = (teacher_id, department_id, institute_id, show_authorised, auth_user_id)
        
        rows = []
        rows = helper.select(db, str_select, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_team_permissions(db, head_id, show_authorised, department_id, institute_id, auth_user_id):
        ''' gets the team permission for the current user '''

        execHelper = ExecHelper()

        str_select = "scheme_of_work__get_team_permissions"
        params = (head_id, department_id, institute_id, show_authorised, auth_user_id)
        
        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting team permissions", e)


    @staticmethod
    def _insert(db, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ inserts the teacher permissions request """
    
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert"
        params = (
            ctx.scheme_of_work_id,
            teacher_id,
            DEPARTMENT(department_permission).value,
            SCHEMEOFWORK(scheme_of_work_permission).value,
            LESSON(lesson_permission).value,
            ctx.auth_user_id,
            is_authorised
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ updates the sow_scheme_of_work__has__teacher """

        execHelper = ExecHelper()
        
        str_update = "scheme_of_work__has__teacher_permission__update"
        params = (
            ctx.scheme_of_work_id,
            teacher_id,
            DEPARTMENT(department_permission).value,
            SCHEMEOFWORK(scheme_of_work_permission).value,
            LESSON(lesson_permission).value,
            ctx.auth_user_id,
            is_authorised
        )

        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, scheme_of_work_id, teacher_id, ctx):
        ''' deletes from sow_scheme_of_work__has__teacher''' 

        execHelper = ExecHelper()

        sql = "scheme_of_work__has__teacher_permission__delete"
        params = (scheme_of_work_id, teacher_id, ctx.auth_user_id)
    
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def insert_access_request(db, scheme_of_work_id, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ inserts the sow_scheme_of_work__has__teacher """
    
        ''' NOTE: get permissions from model '''
        
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert"
        params = (
            scheme_of_work_id,
            teacher_id,
            DEPARTMENT(department_permission).value, # GET PERMISSION FROM MODEL
            SCHEMEOFWORK(scheme_of_work_permission).value, # GET PERMISSION FROM MODEL
            LESSON(lesson_permission).value, # GET PERMISSION FROM MODEL
            ctx.auth_user_id,
            is_authorised
        )
        
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)
        
        return result


    @staticmethod
    def insert_department__has__teacher(db, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ inserts the sow_department__has__teacher """
    
        execHelper = ExecHelper()
        
        sql_insert_statement = "department__has__teacher__insert"
        params = (
            ctx.auth_user_id,
            ctx.department_id,
            DEPARTMENT(department_permission).value,
            SCHEMEOFWORK(scheme_of_work_permission).value,
            LESSON(lesson_permission).value,
            ctx.auth_user_id,
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result