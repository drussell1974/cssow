# -*- coding: utf-8 -*-
import sys
from django.core.exceptions import ValidationError
from django.db import models
from enum import Enum
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.db_helper import ExecHelper, sql_safe
from shared.models.core.basemodel import BaseModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.utils.class_code_generator import ClassCodeGenerator

class TeacherPermissionModel(BaseModel):
    
    class Meta:
        permissions = [('can_manage_team_permissions','Can Manage Team Permissions'), ('can_request_team_permissions','Can Request Team Permissions')]


    @classmethod
    def empty(cls, scheme_of_work, ctx):
        return TeacherPermissionModel(teacher_id=ctx.auth_user_id, teacher_name=ctx.user_name, join_code="", scheme_of_work=scheme_of_work, ctx=ctx) # Default


    @classmethod
    def default(cls, institute, department, scheme_of_work, ctx):        

        teacher_permission = cls.empty(scheme_of_work=scheme_of_work, ctx=ctx)
        teacher_permission.join_code = ClassCodeGenerator.generate_class_code(8)
        # start with no permissions TODO: #373 remove as empty defaults to these values

        teacher_permission.department_permission = DEPARTMENT.NONE
        teacher_permission.scheme_of_work_permission = SCHEMEOFWORK.NONE
        teacher_permission.lesson_permission = LESSON.NONE

        # promote to HOD
        if ctx.auth_user_id is not None and ctx.auth_user_id == department.hod_id:
            ''' set DEPARTMENT.HEAD permissions '''
            teacher_permission.department_permission = DEPARTMENT.HEAD # TODO: #373 DEPARTMENT.HEAD #373 HOD should be administrator
            teacher_permission.scheme_of_work_permission = SCHEMEOFWORK.OWNER
            teacher_permission.lesson_permission = LESSON.OWNER
            teacher_permission.is_authorised = True
            teacher_permission.is_from_db = True
        
        # promote to Admin if creator
        if (ctx.auth_user_id is not None and ctx.auth_user_id == department.created_by_id) or (ctx.auth_user_id is not None and ctx.auth_user_id == institute.created_by_id):        
            teacher_permission.department_permission = DEPARTMENT.ADMIN
            teacher_permission.scheme_of_work_permission = SCHEMEOFWORK.OWNER
            teacher_permission.lesson_permission = LESSON.OWNER
            teacher_permission.is_authorised = True
            teacher_permission.is_from_db = True

        return teacher_permission


    def __init__(self, teacher_id, teacher_name, join_code, scheme_of_work=None, scheme_of_work_permission=SCHEMEOFWORK.NONE, lesson_permission=LESSON.NONE, department_permission=DEPARTMENT.NONE, created=None, auth_user=None, created_by_name=None, published=None, is_from_db=False, is_authorised = False, ctx = None):
        
        #329 Ensure ctx contains institute_id and department_id
        if ctx is None:
            raise KeyError(f"ctx cannot be {ctx}")
        
        super().__init__(teacher_id, teacher_name, created=created, created_by_id=auth_user, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=auth_user)
        
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.join_code = join_code
        self.scheme_of_work_id = scheme_of_work.id if scheme_of_work is not None else 0
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
    
        # teacher required
        self._validate_required_integer("teacher_id", self.teacher_id, 1, BaseModel.MAX_INT)
        # validate required name
        self._validate_required_string("teacher_name", self.teacher_name, 1, 70)
        # validate required join_code
        self._validate_required_string("join_code", self.join_code, 8, 8)
        # validate required department_permission
        self._validate_enum("department_permission", self.department_permission, DEPARTMENT)
        # validate required scheme_of_work_permission
        self._validate_enum("scheme_of_work_permission", self.scheme_of_work_permission, SCHEMEOFWORK)
        # validate required lesson_permission
        self._validate_enum("lesson_permission", self.lesson_permission, LESSON)
        
        # TODO: # validate preset permissions e.g. it should not allow lesser permissions where DEPARTMENT.STUDENT cannot be LESSON.OWNER and SCHEMEOFWORK.OWNER 

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
        is_authorised = self.scheme_of_work_permission % permission == 0 and (self.is_authorised == True or self.is_authorised == 1)
        return is_authorised


    def _check_lesson_permission(self, permission):
        is_authorised = self.lesson_permission % permission == 0 and (self.is_authorised == True or self.is_authorised == 1)
        return is_authorised

    def _check_department_permission(self, permission):
        is_authorised = self.department_permission % permission == 0 and (self.is_authorised == True or self.is_authorised == 1)
        return is_authorised
    

    @staticmethod
    def get_model(db, teacher_id, scheme_of_work, auth_user, show_authorised=True):
        """ get permission for the teacher """
        
        #373 and #363 Get all permissions for department and use dictionary look up on check_permission
        teacher_permissions_dict = {}

        # default or no scheme of work
        teacher_permissions_dict[0] = TeacherPermissionModel.default(institute=auth_user.institute, department=auth_user.department, scheme_of_work=scheme_of_work, ctx=auth_user)
        
        rows = TeacherPermissionDataAccess.get_model(db, teacher_id, auth_user.department_id, auth_user.institute_id, show_authorised=show_authorised, auth_user_id=auth_user.auth_user_id)
        for row in rows:
            # returns only the matching row
            if auth_user.department_id == row[5] and auth_user.institute_id == row[7]:
                cur_scheme_of_work = SchemeOfWorkContextModel(row[3], row[4], auth_user.auth_user_id)
                cur_model = TeacherPermissionModel(teacher_id=teacher_id, teacher_name=row[1], join_code=row[2], scheme_of_work=cur_scheme_of_work,  scheme_of_work_permission=row[9], lesson_permission=row[10], department_permission=row[11], is_from_db=True, is_authorised=row[12], ctx=auth_user)
                # add teacher permission model to dictionary using scheme of work
                teacher_permissions_dict[cur_model.scheme_of_work_id] = cur_model
                # HACK: promote department level permissions for the default permission to highest level of permissions
                if cur_model.department_permission > teacher_permissions_dict[0].department_permission:
                    teacher_permissions_dict[0].department_permission = cur_model.department_permission
                # because the permissions are retrieved from the database set as authorised
                # TODO: Verify if this check is necessary before removing
                teacher_permissions_dict[0].is_authorised = True

        if scheme_of_work.id in teacher_permissions_dict:
            model = teacher_permissions_dict[scheme_of_work.id]
            return model
        else:
            # fall back to default permissions
            model = teacher_permissions_dict[0]
            return model
        

    @staticmethod
    def get_team_permissions(db, teacher_id, auth_user, show_authorised=True):

        cur_scheme_of_work = SchemeOfWorkContextModel.empty()

        rows = TeacherPermissionDataAccess.get_team_permissions(db, teacher_id, show_authorised=show_authorised, department_id=auth_user.department_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows:
            
            # check for changed scheme of work
            if cur_scheme_of_work.id != row[3]:
                cur_scheme_of_work = SchemeOfWorkContextModel(row[3], name=row[4])
                data.append(cur_scheme_of_work)

            model = TeacherPermissionModel(
                teacher_id=row[0],
                teacher_name=row[1], #319 get teacher name
                join_code=row[2],
                scheme_of_work=cur_scheme_of_work,
                department_permission=DEPARTMENT(row[7]),
                scheme_of_work_permission=SCHEMEOFWORK(row[8]),
                lesson_permission=LESSON(row[9]),
                is_authorised=row[10],
                is_from_db = True,
                ctx = auth_user
            )

            cur_scheme_of_work.teacher_permissions.append(model)
            
        return data


    @classmethod
    def get_by_join_code(cls, db, join_code, ctx):


        cur_scheme_of_work = SchemeOfWorkContextModel.empty()

        rows = TeacherPermissionDataAccess.get_by_join_code(db, join_code)
        
        for row in rows:
            # check for changed scheme of work
            if cur_scheme_of_work.id != row[2]:
                cur_scheme_of_work = SchemeOfWorkContextModel(row[3], name=row[4])
            
            model = TeacherPermissionModel(
                teacher_id=row[0],
                teacher_name=row[1], #319 get teacher name
                join_code=row[2],
                scheme_of_work=cur_scheme_of_work,
                department_permission=DEPARTMENT(row[9]),
                scheme_of_work_permission=SCHEMEOFWORK(row[10]),
                lesson_permission=LESSON(row[11]),
                is_authorised=row[12],
                is_from_db = True,
                ctx = ctx
            )

            cur_scheme_of_work.teacher_permissions.append(model)
            return model
        return None


    @staticmethod
    def request_access(db, model, auth_user):

        if model.is_valid:
            TeacherPermissionDataAccess.insert_department__has__teacher(db, model.join_code, DEPARTMENT.NONE, SCHEMEOFWORK.NONE, LESSON.NONE, ctx=auth_user)
            data = TeacherPermissionDataAccess.insert_access_request(db, model.join_code, model.scheme_of_work_id, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, auth_user)
            return data
        return model


    @staticmethod
    def full_access(db, model, auth_user):
        
        if model.is_valid:
            data = TeacherPermissionDataAccess.insert_department__has__teacher(db, model.join_code, DEPARTMENT.ADMIN, SCHEMEOFWORK.OWNER, LESSON.OWNER, ctx=auth_user)
            return data
        return model


    @staticmethod
    def save(db, model, auth_user):
        """ save model """        
        if model.is_new() == False and model.published == STATE.DELETE:
            data = TeacherPermissionDataAccess._delete(db, model.join_code, model.teacher_id, model.is_authorised, ctx=auth_user)
        elif model.is_valid == True:
            if model.is_new() == True:
                data = TeacherPermissionDataAccess._insert(db, model.join_code, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, ctx=auth_user)
                model.id = data[0]
            else:
                data = TeacherPermissionDataAccess._update(db, model.teacher_id, model.department_permission, model.scheme_of_work_permission, model.lesson_permission,  model.is_authorised, ctx=auth_user)
    
        return model


    @staticmethod
    def approve(db, model, auth_user):
        if model.is_authorised == True and model.is_valid == True:
            TeacherPermissionDataAccess.approve_access_request(db, model.scheme_of_work_id, model.teacher_id, model.join_code, model.department_permission, model.scheme_of_work_permission, model.lesson_permission, ctx=auth_user)
    
        return model


    @staticmethod
    def delete(db, model, auth_user):
        TeacherPermissionDataAccess._delete(db, model.join_code, model.teacher_id, model.is_authorised, ctx=auth_user)
        model.is_from_db = False
        return model


class TeacherPermissionDataAccess:

    @staticmethod
    def get_model(db, teacher_id, department_id, institute_id, show_authorised, auth_user_id):
        ''' gets the current users permissions for the scheme of work  '''
        
        helper = ExecHelper()

        str_select = "scheme_of_work__get_teacher_permissions$2"
        
        params = (teacher_id, department_id, institute_id, show_authorised, auth_user_id)
        
        rows = []
        rows = helper.select(db, str_select, params, rows, handle_log_info)
        
        return rows


    @staticmethod
    def get_team_permissions(db, head_id, show_authorised, department_id, institute_id, auth_user_id):
        ''' gets the team permission for the current user '''

        execHelper = ExecHelper()

        str_select = "scheme_of_work__get_team_permissions$2"
        params = (head_id, department_id, institute_id, show_authorised, auth_user_id)
        
        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting team permissions", e)


    @staticmethod
    def get_by_join_code(db, join_code):
        ''' gets the team permission for the new user '''

        execHelper = ExecHelper()

        str_select = "scheme_of_work__get_team_permissions_by_join_code"
        params = (join_code, True, 0)
        
        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise PermissionError("Error getting team permissions", e)


    @staticmethod
    def _insert(db, join_code, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ inserts the teacher permissions request """
    
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert$2"
        params = (
            teacher_id,
            ctx.scheme_of_work_id,
            join_code,
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
        
        str_update = "scheme_of_work__has__teacher_permission__update$2"
        params = (
            ctx.department_id,
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
    def _delete(db, join_code, teacher_id, is_authorised, ctx):
        ''' deletes from sow_scheme_of_work__has__teacher''' 

        execHelper = ExecHelper()

        sql = "scheme_of_work__has__teacher_permission__delete$2"
        params = (join_code, teacher_id, is_authorised, ctx.auth_user_id)
    
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def insert_access_request(db, join_code, scheme_of_work_id, teacher_id, department_permission, scheme_of_work_permission, lesson_permission, is_authorised, ctx):
        """ inserts the sow_scheme_of_work__has__teacher """
    
        ''' NOTE: get permissions from model '''
        
        execHelper = ExecHelper()

        sql_insert_statement = "scheme_of_work__has__teacher_permission__insert$2"
        params = (
            teacher_id,
            scheme_of_work_id,
            join_code,
            DEPARTMENT(department_permission).value, # GET PERMISSION FROM MODEL
            SCHEMEOFWORK(scheme_of_work_permission).value, # GET PERMISSION FROM MODEL
            LESSON(lesson_permission).value, # GET PERMISSION FROM MODEL
            ctx.auth_user_id,
            is_authorised
        )    
        
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)
        
        return result


    @staticmethod
    def approve_access_request(db, scheme_of_work_id, teacher_id, join_code, department_permission, scheme_of_work_permission, lesson_permission, ctx):
        """ update the sow_scheme_of_work__has__teacher """
        
        execHelper = ExecHelper()

        sql_update_statement = "scheme_of_work__has__teacher_permission__approve$2"
        params = (
            ctx.department_id,
            scheme_of_work_id,
            teacher_id,
            join_code,
            DEPARTMENT(department_permission).value, # GET PERMISSION FROM MODEL
            SCHEMEOFWORK(scheme_of_work_permission).value, # GET PERMISSION FROM MODEL
            LESSON(lesson_permission).value, # GET PERMISSION FROM MODEL
            ctx.auth_user_id
        )    
        
        result = execHelper.update(db, sql_update_statement, params, handle_log_info)
        
        return result


    @staticmethod
    def insert_department__has__teacher(db, join_code, department_permission, scheme_of_work_permission, lesson_permission, ctx):
        """ inserts the sow_department__has__teacher """
    
        execHelper = ExecHelper()
        
        sql_insert_statement = "department__has__teacher__insert$2"
        params = (
            ctx.auth_user_id,
            ctx.department_id,
            join_code,
            DEPARTMENT(department_permission).value,
            SCHEMEOFWORK(scheme_of_work_permission).value,
            LESSON(lesson_permission).value,
            ctx.auth_user_id,
        )

        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result
