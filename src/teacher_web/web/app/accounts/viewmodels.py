"""
View Models
"""
import io
from rest_framework import serializers, status
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_registereduser import RegisteredUserModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

# TODO: 206 inherit RegisteredUserForm from UserCreationForm to include new fields

class RegisterUserForm(UserCreationForm):
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = RegisteredUserModel
        fields = ('first_name','last_name','email',)
        #username = models.CharField(max_length=30, required=False, help_text='Optional.')
        #first_name = models.CharField(max_length=30, required=False, help_text='Optional.')
        #last_name = models.CharField(max_length=30, required=False, help_text='Optional.')
        #email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        #is_staff = models.BooleanField(required=True, help_text="Check if this is a staff member. You must also set permissions.")
        #is_active = models.BooleanField(required=True, help_text="Chack to set the user account active")


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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
        
        return RegisterIndexViewModel.as_view()
        data = {
            "form": self.model
        }
        return ViewModel("Dave Russell - Teach Computer Science", "Account", "Registration", data = data, error_message=self.error_message)
