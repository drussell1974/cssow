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
from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON, parse_enum
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class TeamPermissionIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, auth_user):
        #super().__init__(ctx=auth_user)
        self.db = db
        self.request = request
        self.auth_user = auth_user

    def view(self):

        authorised_permissions = TeacherPermissionModel.get_team_permissions(self.db, self.auth_user.auth_user_id, self.auth_user, True)

        pending_permissions = TeacherPermissionModel.get_team_permissions(self.db, self.auth_user.auth_user_id, self.auth_user, False)

        data = {
                "authorised_permissions": authorised_permissions,
                "pending_permissions": pending_permissions
            }
        
        return ViewModel("Account", "Account", "Team Permissions", ctx=self.auth_user, data=data)


class TeamPermissionEditViewModel(BaseViewModel):
    
    def __init__(self, db, request, scheme_of_work_id, teacher_id, auth_user):
    
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.teacher_id = teacher_id
        self.auth_user = auth_user
        
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        # Http404
        
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        
        # get the permissions for the selected teacher
        self.model = TeacherPermissionModel.get_model(db, teacher_id=teacher_id, scheme_of_work=self.scheme_of_work, auth_user=auth_user, show_authorised=1)
    
        if self.teacher_id > 0:
            if self.model is None or self.model.is_from_db == False:
                self.on_not_found(self.model, teacher_id)
        
        
    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "scheme_of_work_name":self.scheme_of_work.name,
            "department_permission": self.model.department_permission,
            "scheme_of_work_permission": self.model.scheme_of_work_permission,
            "lesson_permission": self.model.lesson_permission,
            "department_permission_options": list(DEPARTMENT),
            "scheme_of_work_permission_options": list(SCHEMEOFWORK),
            "lesson_permission_options": list(LESSON),
            "model": self.model
        }

        return ViewModel("Account", "Account", "Team Permissions", ctx=self.auth_user, data=data, active_model=self.model)


    def execute(self):
        
        self.model.department_permission = self.request.POST.get("department_permission", 0)
        self.model.scheme_of_work_permission = self.request.POST.get("scheme_of_work_permission", 0)
        self.model.lesson_permission = self.request.POST.get("lesson_permission", 0)

        self.model.validate()
        
        if self.model.is_valid == True:
            
            ''' explicitly authorise '''

            self.model.is_authorised = True

            TeacherPermissionModel.save(self.db, self.model, self.auth_user)

            self.on_post_complete(True)
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving team permission", "permission settings are not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))
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

        # get the permissions for the selected teacher
        self.model = TeacherPermissionModel.get_model(db, teacher_id=teacher_id, scheme_of_work=self.scheme_of_work, auth_user=auth_user, show_authorised=1)

        # Http404
        if self.scheme_of_work_id > 0 and teacher_id > 0:
            if self.model is None or self.model.is_from_db == False:
                self.on_not_found(self.model, self.scheme_of_work_id, self.teacher_id)


    def execute(self):
        if self.model is not None:
            # can now delete    
            self.model = TeacherPermissionModel.delete(db, self.model, self.auth_user)


class TeamPermissionRequestAccessViewModel(BaseViewModel):

    def __init__(self, db, request, scheme_of_work_id, teacher_name, permission, auth_user):
        super().__init__(auth_user)
        self.scheme_of_work_id = scheme_of_work_id
        #self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.permission = parse_enum(permission)
        self.auth_user = auth_user

        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        
        # Http404
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        
        # get the permissions for the current user
        self.model = TeacherPermissionModel.get_model(db, teacher_id=auth_user.auth_user_id, scheme_of_work=self.scheme_of_work, auth_user=auth_user)

        # Check if permission has already been granted
        self.model.validate()
        if self.model is not None and self.model.is_from_db == True and self.model.is_authorised == True:
            raise PermissionError(f"{teacher_name} has already been granted access to this scheme of work.")
        
        self.model = TeacherPermissionModel(
            teacher_id=self.model.teacher_id,
            teacher_name=self.model.teacher_name,
            scheme_of_work=self.scheme_of_work, 
            department_permission = self.permission if type(self.permission) is DEPARTMENT else DEPARTMENT.NONE,
            scheme_of_work_permission = self.permission if type(self.permission) is SCHEMEOFWORK else SCHEMEOFWORK.NONE,
            lesson_permission = self.permission if type(self.permission) is LESSON else LESSON.NONE,
            is_authorised=False,
            ctx=auth_user
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
        
        self.institute_id = kwargs["institute_id"] 
        self.department_id = kwargs["department_id"] 
        self.scheme_of_work_id = kwargs["scheme_of_work_id"] 
        self.teacher_id = auth_user.auth_user_id
        self.request_made = False
        
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, self.scheme_of_work_id, auth_user=auth_user)
        
        # Http404
        if self.scheme_of_work.id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)
        
        # get the permissions for the selected teacher
        self.model = TeacherPermissionModel.get_model(db, teacher_id=self.teacher_id, scheme_of_work=self.scheme_of_work, auth_user=auth_user)    
        
        # Check if permission has already been granted
        if self.model.teacher_id is not None:
            if self.model.teacher_id > 0:
                self.model.validate()
                if self.model is not None and self.model.is_from_db == True and self.model.is_authorised is False:
                    self.request_made = True
        
        kwargs = dict(**kwargs, request_made=self.request_made)

        self.context = get_context_data(**kwargs)


    def view(self):
        return self.context

        