import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from .viewmodels import RegisterUserForm

from shared.view_model import ViewModel

# Create your views here.
@login_required()
def index(request):
    return render(request, "accounts/index.html")

def my_team_permissions(request):

    content = None

    return render(request, "accounts/my_team_permissions.html", content)    


class RegisterUserView(generic.CreateView):
    # 206 inherit RegisteredUserForm from UserCreationForm - see .viewmodels.py
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
