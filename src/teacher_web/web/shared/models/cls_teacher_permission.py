# -*- coding: utf-8 -*-
from django.db import models
from enum import Enum
from shared.models.core.log import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

class TeacherPermissionModel(models.Model):

    def __init__(self, auth_user, auth_user_name, scheme_of_work, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE, department_permission=DEPARTMENT.NONE, published = 0, is_from_db=False):
        self.teacher_id = auth_user
        self.auth_user_name = auth_user_name
        self.scheme_of_work = scheme_of_work
        self.scheme_of_work_permission = scheme_of_work_permission
        self.lesson_permission = lesson_permission
        self.department_permission = department_permission
        self.published = published
        self.is_from_db = is_from_db


    def is_new(self):
        return (self.is_from_db == False)
        

    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """
        self.teacher = int(self.teacher)
        # TODO: #316 - clean auth_user_name


    def check_permission(self, permission):
        if type(permission) == SCHEMEOFWORK:
            return self._check_scheme_of_work_permission(permission)
        elif type(permission) == LESSON:
            return self._check_lesson_permission(permission)
        elif type(permission) == DEPARTMENT:
            return self._check_department_permission(permission)
        else:
            raise TypeError("permission is type {}. Must be type SCHEME_OF_WORK or LESSON_ACCESS.".format(type(permission)))


    def _check_scheme_of_work_permission(self, permission):
        return self.scheme_of_work_permission % permission == 0


    def _check_lesson_permission(self, permission):
        return self.lesson_permission % permission == 0


    def _check_department_permission(self, permission):
        return self.department_permission % permission == 0


    @staticmethod
    def get_model(db, scheme_of_work, auth_user):
        rows = TeacherPermissionDataAccess.get_model(db, scheme_of_work.id, auth_user)
        model = TeacherPermissionModel(auth_user=auth_user, auth_user_name="", scheme_of_work=scheme_of_work) # Default
        for row in rows:
            model = TeacherPermissionModel(auth_user=auth_user, auth_user_name="", scheme_of_work=scheme_of_work, scheme_of_work_permission=row[0], lesson_permission=row[1], department_permission=row[2])
            return model
            
        return model


    @staticmethod
    def get_team_permissions(db, auth_user):

        cur_scheme_of_work = SchemeOfWorkModel(0)

        rows = TeacherPermissionDataAccess.get_team_permissions(db, auth_user)
        data = []
        for row in rows:
            
            # check for changed scheme of work
            if cur_scheme_of_work.id != row[2]:
                cur_scheme_of_work = SchemeOfWorkModel(row[2], name=row[3])
                data.append(cur_scheme_of_work)


            model = TeacherPermissionModel(
                auth_user=row[0],
                auth_user_name=row[1],
                scheme_of_work=cur_scheme_of_work,
                department_permission=DEPARTMENT(row[4]),
                scheme_of_work_permission=SCHEMEOFWORK(row[5]),
                lesson_permission=LESSON(row[6])
            )

            cur_scheme_of_work.teacher_permissions.append(model)

        return data


    @staticmethod
    def save(db, model, auth_user):
        """ save model """
        if model.is_new() == False and model.published == 2:
            data = TeacherPermissionDataAccess._delete(db, model, auth_user)
        else:
            if model.is_new() == True:
                data = TeacherPermissionDataAccess._insert(db, model, auth_user)
                model.id = data[0]
            else:
                data = TeacherPermissionDataAccess._update(db, model, auth_user)
    
        return model


class TeacherPermissionDataAccess:

    @staticmethod
    def get_model(db, scheme_of_work_id, auth_user):
        ''' gets the current users permissions for the scheme of work  '''

        helper = ExecHelper()

        str_select = "scheme_of_work__get_teacher_permissions"
        params = (scheme_of_work_id, auth_user)
        
        rows = []
        rows = helper.select(db, str_select, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_team_permissions(db, user_auth):
        ''' gets the team permission for the current user '''

        execHelper = ExecHelper()

        str_select = "scheme_of_work__get_team_permissions"
        params = (user_auth,)

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

        sql_insert_statement = "scheme_of_work__has__teacher__insert"
        params = (
            model.scheme_of_work.id,
            model.teacher_id,
            model.department_permission,
            model.scheme_of_work_permission,
            model.lesson_permission,
            auth_user
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, auth_user):
        """ updates the sow_scheme_of_work__has__teacher """
        
        execHelper = ExecHelper()
        
        str_update = "scheme_of_work__has__teacher__update"
        params = (
            model.scheme_of_work.id,
            model.teacher_id,
            model.department_permission,
            model.scheme_of_work_permission,
            model.lesson_permission,
            auth_user
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user):
        ''' deletes from sow_scheme_of_work__has__teacher''' 

        execHelper = ExecHelper()

        sql = "scheme_of_work__has__teacher__delete"
        params = (model.scheme_of_work.id, model.teacher_id, auth_user)
    
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows
