"""
View Models
"""
import io
from rest_framework import serializers, status
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import connection as db
from django.urls import reverse
from django.conf import settings
from shared.models.core.basemodel import try_int
from shared.models.core.context import Ctx
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_error, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_notification import NotifyModel
from shared.models.cls_pathway_template import PathwayTemplateModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class AccountIndexViewModel(BaseViewModel):
    
    def __init__(self, db, top, auth_user):
        self.db = db
        self.auth_user = auth_user

        try:
            # get institutes
            self.institutes = InstituteModel.get_my(self.db, auth_user=auth_user)

        except Exception as e:
            self.error_message = repr(e)


    def view(self, request):
        
        data = {
            "institutes": self.institutes,
        }
        
        return ViewModel(request, "", "Account", settings.SITE_TITLE, ctx=self.auth_user, data=data, error_message=self.error_message)


class AccountDeleteViewModel(BaseViewModel):

    def __init__(self, db, request):
        self.db = db
        self.model = request.user 
        

    def execute(self):
        TeacherModel.save(self.db, self.model)


    def view(self, request):    
        return ViewModel(request, "",self.model.username, "Account", ctx=self.model)


class RegisterTeacherForm(UserCreationForm):

    first_name = forms.CharField(label='Display name', max_length=150, required=True, help_text="required")
    ''' Email used as user name so limit to 150 characters '''
    email = forms.EmailField(label='Email', max_length=150, required=True, help_text='required') 
    department_name = forms.CharField(label='Department name (teachers only)', max_length=70, required=False, help_text="your department name")
    institute_name = forms.CharField(label='Institute name (teachers only)', max_length=70, required=False, help_text="your institute/school name")
    pathway_id = forms.ChoiceField(choices=PathwayTemplateModel.get_options(db))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','first_name', 'institute_name', 'department_name', 'pathway_id')
    

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]
        user.set_password(password)
        user.username = self.cleaned_data["email"]
        user.department_name = self.cleaned_data["department_name"]
        user.institute_name = self.cleaned_data["institute_name"]

        # TODO: #256 create select option on ui page use PathwayTemplateModel.get_options()

        pathway_id =  self.cleaned_data["pathway_id"]

        if commit:
            user.save()
            auth_ctx = Ctx(0, 0, auth_user_id=user.id)
            
            # initialise here for reference in exception
            institute_model = None
            department_model = None

            try:
            
                # a newly registered user is always head of department and teacher
                
                teacher_group = Group.objects.get(name='head of department')
                teacher_group.user_set.add(user)
                teacher_group = Group.objects.get(name='teacher')
                teacher_group.user_set.add(user)

                # create institute instances
                
                institute_name = user.institute_name if len(user.institute_name) > 0 else user.username
                institute_model = InstituteModel(0, name=institute_name, published=STATE.PUBLISH)

                # create department instance

                department_name = user.department_name if len(user.department_name) > 0 else user.username
                department_model = DepartmentModel(0, name=department_name, topic_id = 0, institute = institute_model, ctx=auth_ctx, published=STATE.PUBLISH)

                # create teacher permission

                teacher_permission_model = TeacherPermissionModel(user.id, user.username, is_authorised=True, ctx=auth_ctx)
                teacher_permission_model.department_permission = DEPARTMENT.ADMIN
                teacher_permission_model.scheme_of_work_permission = SCHEMEOFWORK.OWNER
                teacher_permission_model.lesson_permission = LESSON.OWNER

                # validate

                institute_model.validate()
                department_model.validate()
                teacher_permission_model.validate()
                
                # save if all are valid

                if institute_model.is_valid and department_model.is_valid and teacher_permission_model.is_valid:

                    # save the institute
                    institute_model = InstituteModel.save(db, institute_model, user.id, auth_user=auth_ctx)
                    # set the institute id context
                    auth_ctx.institute_id = institute_model.id
                    department_model.institute_id = institute_model.id

                    # save the department
                    department_model = DepartmentModel.save(db, department_model, user.id, auth_user=auth_ctx)
                    # set the department id context
                    auth_ctx.department_id = department_model.id

                    # create pathways/key_stage available
                    
                    ''' this creates the available key stages and levels for the department '''

                    pathway = PathwayTemplateModel(id_=pathway_id, name="", department_id=department_model.id)
                    pathway = PathwayTemplateModel.save(db, pathway, auth_user=auth_ctx)
                    
                    pathway.validate()

                    if pathway.is_valid:
                        # insert department permissions
                        TeacherPermissionModel.full_access(db, teacher_permission_model, auth_user=auth_ctx)
                    else:
                        # delete user if cannot create department
                        if user.id is not None:
                            user.delete()
        
                else:
                    # delete user if cannot create department
                    if user.id is not None:
                        user.delete()

            except Exception as e:
                # delete user if cannot create department
                if user.id is not None:
                    user.delete()
                    
                # delete department
                if department_model is not None:
                    department_model.published = STATE.DELETE
                    DepartmentModel.save(db, department_model, user.id, auth_ctx)

                # delete institute
                if institute_model is not None:
                    institute_model.published = STATE.DELETE
                    InstituteModel.save(db, institute_model, user.id, auth_ctx)
                
                raise Exception("An error occurred creating user.") from e

        return user


class JoinAsTeacherForm(UserCreationForm):
    pass