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
from shared.models.core.basemodel import try_int
from shared.models.core.context import Ctx
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher_permission import TeacherPermissionModel

from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

# 206 inherit RegisteredUserForm from UserCreationForm to include new fields
class RegisterTeacherForm(UserCreationForm):

    first_name = forms.CharField(label='Display name', max_length=150, required=True, help_text="required")
    ''' Email used as user name so limit to 150 characters '''
    email = forms.EmailField(label='Email', max_length=150, required=True, help_text='required') 
    role = forms.ChoiceField(label='What is your role?', choices=((1, "I am a teacher"), (2,"I am a student"))) 
    department_name = forms.CharField(label='Department name (teachers only)', max_length=70, required=False, help_text="your department name")
    institute_name = forms.CharField(label='Institute name (teachers only)', max_length=70, required=False, help_text="your institute/school name")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','first_name', 'role', 'institute_name', 'department_name')
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]
        user.set_password(password)
        user.username = self.cleaned_data["email"]
        user.role = self.cleaned_data["role"]
        user.department_name = self.cleaned_data["department_name"]
        user.institute_name = self.cleaned_data["institute_name"]

        if commit:
            user.save()
            auth_ctx = Ctx(0, 0, auth_user_id=user.id)
            
            # initialise here for reference in exception
            institute_model = None
            department_model = None

            try:
                if try_int(user.role) == 0:
                    
                    teacher_group = Group.objects.get(name='student')
                    teacher_group.user_set.add(user)

                elif try_int(user.role) == 1:

                    # a newly registered user is always head of department and teacher
                    
                    teacher_group = Group.objects.get(name='head of department')
                    teacher_group.user_set.add(user)
                    teacher_group = Group.objects.get(name='teacher')
                    teacher_group.user_set.add(user)

                    # create institute instances
                    
                    institute_name = user.institute_name if len(user.institute_name) > 0 else user.username
                    institute_model = InstituteModel(0, name=institute_name, published=1)

                    # create department instance

                    department_name = user.department_name if len(user.department_name) > 0 else user.username
                    department_model = DepartmentModel(0, name=department_name, institute = institute_model, ctx=auth_ctx, published=1)

                    # create teacher permission
                    teacher_permission_model = TeacherPermissionModel(user.id, user.username, is_authorised=True, ctx=auth_ctx)
                    teacher_permission_model.department_permission = DEPARTMENT.ADMIN
                    teacher_permission_model.scheme_of_work_permission = SCHEMEOFWORK.OWNER
                    teacher_permission_model.lesson_permission = LESSON.OWNER

                    # validate

                    institute_model.validate()
                    department_model.validate()
                    teacher_permission_model.validate()
                    # save

                    if institute_model.is_valid and department_model.is_valid and teacher_permission_model.is_valid:

                        # save the institute
                        institute_model = InstituteModel.save(db, institute_model, user.id, auth_user=auth_ctx)
                        # set the institute id context
                        auth_ctx.institute_id = institute_model.id
            
                        # save the department
                        department_model = DepartmentModel.save(db, department_model, user.id, auth_user=auth_ctx)
                        # set the department id context
                        auth_ctx.department_id = department_model.id

                        # insert department permissions
                        
                        TeacherPermissionModel.full_access(db, teacher_permission_model, auth_user=auth_ctx)
                        
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
