"""
View Models
"""
import io
from rest_framework import serializers, status
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import connection as db
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

# 206 inherit RegisteredUserForm from UserCreationForm to include new fields
class RegisterUserForm(UserCreationForm):
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
            user.save()
            
            # a newly registered user is always head of department
            
            teacher_group = Group.objects.get(name='head of department')
            teacher_group.user_set.add(user)

            # new department 
            
            model = DepartmentModel(0, user.department_name if user.department_name is not None else user.username)           
            model.school_id = 0            
            # save
            DepartmentModel.save(db, model, user.id, user.id)

        return user
