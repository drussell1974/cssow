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
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_department import DepartmentModel
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
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','first_name', 'role', 'department_name')
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["email"]
        user.role = self.cleaned_data["role"]
        user.department_name = self.cleaned_data["department_name"]

        if commit:
            try:
                user.save()
                
                # a newly registered user is always head of department
                
                teacher_group = Group.objects.get(name='head of department')
                teacher_group.user_set.add(user)

                # new department 
                
                ''' default department name to username and school id to user id '''
                department_name = user.department_name if len(user.department_name) > 0 else user.username

                model = DepartmentModel(0, name=department_name, school_id=user.id)

                model.validate()
                
                # save
                if model.is_valid:
                    DepartmentModel.save(db, model, user.id, user.id)
                else:
                    # delete user if cannot create department
                    if user.id is not None:
                        user.delete()
                
            except Exception as e:
                # delete user if cannot create department
                if user.id is not None:
                    user.delete()
                raise Exception("An error occurred creating user")

        return user
