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
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning, handle_log_error
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

# 206 inherit RegisteredUserForm from UserCreationForm to include new fields
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Display name', max_length=150, required=True, help_text="required")
    ''' Email used as user name so limit to 150 characters '''
    email = forms.EmailField(label='Email', max_length=150, required=True, help_text='required') 

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','first_name',) #, 'memorable_word_1', 'memorable_word_2')
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        #display_name = display_name + "xxx"
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
            teacher_group = Group.objects.get(name='teacher')
            teacher_group.user_set.add(user)
        return user
