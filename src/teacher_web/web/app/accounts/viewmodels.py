"""
View Models
"""
import io
from rest_framework import serializers, status
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_registereduser import RegisteredUserModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

# TODO: 206 inherit RegisteredUserForm from UserCreationForm to include new fields
class RegisterUserForm(UserCreationForm):
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    #username = forms.CharField(max_length=150, label='User name', required=True, help_text='required')
    first_name = forms.CharField(label='Display name', max_length=150, required=True, help_text="required")
    #last_name = forms.CharField(max_length=150, required=False)
    ''' Email used as user name so limit to 150 characters '''
    email = forms.EmailField(label='Email', max_length=150, required=True, help_text='required') 
    #memorable_word = forms.CharField(max_length=150, required=True, help_text='required to retrieve your password')
    #memorable_word_2 = forms.CharField(max_length=150, help_text='required.', widget=forms.PasswordInput)

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
        return user

'''
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

'''

# TODO: 206 inherit RegisteredUserForm from UserCreationForm may not required AccountsRegiterViewModel
class AccountsRegisterViewModel(BaseViewModel):

    def __init__(self, db, request):
        self.db = db
        self.request = request
        self.model = UserCreationForm()
        
        
    def execute(self):
        self.model = UserCreationForm(self.request.POST)

        if self.request.method == "POST":
            if self.model.is_valid() == True:
                self.model.save()
            else:
                raise AttributeError("not valid")
                

    def view(self):
        
        data = {
            "form": self.model
        }
        return ViewModel("Dave Russell - Teach Computer Science", "Account", "Registration", data = data, error_message=self.error_message)
