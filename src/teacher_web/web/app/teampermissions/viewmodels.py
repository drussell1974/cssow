"""
View Models
"""
from rest_framework import serializers, status
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import connection as db
from django.http import Http404
from shared.models.core.basemodel import try_int
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON, parse_enum
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class TeamPermissionIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, auth_user):
        self.db = db
        self.request = request
        self.auth_user = auth_user


    def view(self):

        departments = TeacherPermissionModel.get_team_permissions(self.db, self.auth_user, self.auth_user)

        data = {
                "my_team_permissions": departments,
            }

        return ViewModel("Account", "Account", "Team Permissions", data=data)


class TeamPermissionEditViewModel(BaseViewModel):
   
    def __init__(self, db, request, scheme_of_work_id, teacher_id, auth_user):

        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        
        department = DepartmentModel(0, "")
        teacher = TeacherModel(0, "", department)

        # Http404
        '''
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        '''
        # TODO: #329 pass e.g. teacher=TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science"))
        self.model = TeacherPermissionModel.get_model(db, self.scheme_of_work, teacher=teacher, auth_user=auth_user)
        '''
        if self.scheme_of_work_id > 0 and teacher_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        '''
        
        self.auth_user = auth_user
        
    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "scheme_of_work_name":self.scheme_of_work.name,
            "teacher_id": self.model.teacher_id,
            "teacher_name": self.model.teacher.get_name(),
            "department_permission": self.model.department_permission,
            "scheme_of_work_permission": self.model.scheme_of_work_permission,
            "lesson_permission": self.model.lesson_permission,
            "department_permission_options": list(DEPARTMENT),
            "scheme_of_work_permission_options": list(SCHEMEOFWORK),
            "lesson_permission_options": list(LESSON),
            "model": self.model
        }

        return ViewModel("Account", "Account", "Team Permissions", data=data, active_model=self.model)


    def execute(self):
        
        self.model.department_permission = self.request.POST.get("department_permission", 0)
        self.model.scheme_of_work_permission = self.request.POST.get("scheme_of_work_permission", 0)
        self.model.lesson_permission = self.request.POST.get("lesson_permission", 0)

        self.model.validate()
        
        if self.model.is_valid == True:
            
            ''' explicitly authorise '''

            self.model.is_authorised = True

            data = TeacherPermissionModel.save(self.db, self.model, self.auth_user)

            self.on_post_complete(True)
        else:
            # TODO: #318 - log by department/user_
            #handle_log_warning(self.db, self.scheme_of_work_id, "saving learning objective", "permission settings are not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))
            pass
        
        return self.view()


class TeamPermissionDeleteViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, teacher_id, auth_user):
        self.teacher_id = teacher_id
        self.scheme_of_work_id = scheme_of_work_id
        self.auth_user = auth_user

        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        
        # Http404
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)

        self.model = TeacherPermissionModel.get_model(db, self.scheme_of_work, teacher_id=teacher_id, auth_user=auth_user)

        # Http404
        if self.scheme_of_work_id > 0 and teacher_id > 0:
            if self.model is None or self.model.is_from_db == False:
                self.on_not_found(self.model, self.teacher_id)


    def execute(self):
        if self.model is not None:
            # can now delete    
            self.model = TeacherPermissionModel.delete(db, self.model, self.auth_user)


class TeamPermissionRequestAccessViewModel(BaseViewModel):

    def __init__(self, db, request, scheme_of_work_id, teacher_id, teacher_name, permission, auth_user):
        
        self.scheme_of_work_id = scheme_of_work_id
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.permission = parse_enum(permission)
        self.auth_user = auth_user

        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        
        # Http404
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)

        self.model = TeacherPermissionModel.get_model(db, self.scheme_of_work, teacher=auth_user, auth_user=auth_user)
    
        # Check if permission has already been granted
        if self.teacher_id > 0:
            self.model.validate()
            if self.model is not None and self.model.is_from_db == True and self.model.is_authorised == True:
                raise PermissionError(f"{teacher_name} has already been granted access to this scheme of work.")

        self.model = TeacherPermissionModel(
            scheme_of_work=self.scheme_of_work, 
            # TODO: #329 pass e.g. teacher=TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science"))
            teacher=self.model.teacher,
            is_authorised=False,
            department_permission = self.permission if type(self.permission) is DEPARTMENT else DEPARTMENT.NONE,
            scheme_of_work_permission = self.permission if type(self.permission) is SCHEMEOFWORK else SCHEMEOFWORK.NONE,
            lesson_permission = self.permission if type(self.permission) is LESSON else LESSON.NONE
        )
        

    def execute(self):

        if self.model.validate():
            # can now request access
            self.model = TeacherPermissionModel.request_access(db, self.model, self.auth_user)
        else:
            raise ValidationError(self.model.validation_errors)


class TeamPermissionRequestLoginViewModel(AuthenticationForm):
    def __init__(self, db, request, get_context_data, auth_user, **kwargs):
        super().__init__(request)
        
        self.scheme_of_work_id = kwargs["scheme_of_work_id"] 
        self.teacher_id = auth_user
        self.request_made = False
        
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        # Http404
        if self.scheme_of_work.id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        
        self.model = TeacherPermissionModel.get_model(db, self.scheme_of_work, teacher=auth_user, auth_user=auth_user)    
        # Check if permission has already been granted
        if self.model.teacher.id is not None and self.model.teacher.id > 0:
            self.model.validate()
            if self.model is not None and self.model.is_from_db == True and self.model.is_authorised is False:
                self.request_made = True
        
        kwargs = dict(**kwargs, request_made=self.request_made)

        self.context = get_context_data(**kwargs)


    def view(self):
        return self.context

        