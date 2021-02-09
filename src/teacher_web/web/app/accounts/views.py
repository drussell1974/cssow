import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from shared.view_model import ViewModel

from .viewmodels import RegisterTeacherForm

# Create your views here.
@login_required()
def index(request):
    return render(request, "accounts/index.html")


class RegisterTeacherView(generic.CreateView):
    # 206 inherit RegisteredUserForm from UserCreationForm - see .viewmodels.py
    form_class = RegisterTeacherForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
