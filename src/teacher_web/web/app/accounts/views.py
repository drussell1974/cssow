import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic

# TODO: 206 inherit RegisteredUserForm from UserCreationForm - comment out line below
from django.contrib.auth.forms import UserCreationForm
# TODO: 206 uncomment
# from .viewmodels import AccountsRegisterViewModel

from shared.view_model import ViewModel

# Create your views here.
@login_required()
def index(request):
    return render(request, "accounts/index.html")
    

class RegisterUserView(generic.CreateView):
    # TODO: 206 inherit RegisteredUserForm from UserCreationForm - see .viewmodels.py
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
