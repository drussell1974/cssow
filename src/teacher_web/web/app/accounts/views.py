import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from shared.models.core.context import AuthCtx
from shared.view_model import ViewModel

from .viewmodels import RegisterTeacherForm, AccountIndexViewModel

# Create your views here.
@login_required()
def index(request):

    # TODO: Get institute for current user
    
    auth_ctx = AuthCtx(db, request, 0, 0)
    
    # get the schemes of work
    #253 check user id
    modelview = AccountIndexViewModel(db=db, top=5, auth_user=auth_ctx)
    
    view_model = modelview.view(os.environ["TEACHER_WEB__SITE_TITLE"], os.environ["TEACHER_WEB__SITE_SUMMARY"])

    return render(request, "accounts/index.html", view_model.content)


class RegisterTeacherView(generic.CreateView):
    # 206 inherit RegisteredUserForm from UserCreationForm - see .viewmodels.py
    form_class = RegisterTeacherForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'
