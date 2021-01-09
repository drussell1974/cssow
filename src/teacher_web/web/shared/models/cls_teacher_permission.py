# -*- coding: utf-8 -*-
from django.db import models
from enum import Enum
from shared.models.core.log import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON

class TeacherPermissionModel(models.Model):

    def __init__(self, auth_user, scheme_of_work_id, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE):
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.scheme_of_work_permission = scheme_of_work_permission
        self.lesson_permission = lesson_permission


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """
        self.auth_user = int(self.auth_user)


    def check_permission(self, permission):
        if type(permission) == SCHEMEOFWORK:
            return self._check_scheme_of_work_permission(permission)
        elif type(permission) == LESSON:
            return self._check_lesson_permission(permission)
        else:
            raise TypeError("permission is type {}. Must be type SCHEME_OF_WORK or LESSON_ACCESS.".format(type(permission)))


    def _check_scheme_of_work_permission(self, permission):
        return self.scheme_of_work_permission % permission == 0


    def _check_lesson_permission(self, permission):
        return self.lesson_permission % permission == 0
        

    @staticmethod
    def get_model(db, scheme_of_work_id, auth_user):
        rows = TeacherPermissionDataAccess.get_model(db, scheme_of_work_id, auth_user)
        model = TeacherPermissionModel(auth_user=auth_user, scheme_of_work_id=scheme_of_work_id) # Default
        for row in rows:
            model = TeacherPermissionModel(auth_user=auth_user, scheme_of_work_id=scheme_of_work_id, scheme_of_work_permission=row[0], lesson_permission=row[1])
        return model


class TeacherPermissionDataAccess:

    @staticmethod
    def get_model(db, scheme_of_work_id, auth_user):
        helper = ExecHelper()

        str_select = "scheme_of_work__get_teacher_permissions"
        params = (scheme_of_work_id, auth_user)
        rows = []
        rows = helper.select(db, str_select, params, rows, handle_log_info)
        
        return rows