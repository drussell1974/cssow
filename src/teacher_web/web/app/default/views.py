import os
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse
from shared.models.core.django_helper import auth_user_id

from shared.view_model import ViewModel
from .viewmodels import SchemeOfWorkGetLatestViewModel

# Create your views here.
def index(request):

    # get the schemes of work
    #253 check user id
    modelview = SchemeOfWorkGetLatestViewModel(db, top = 5, auth_user=auth_user_id(request))
    
    view_model = modelview.view(os.environ["TEACHER_WEB__SITE_TITLE"], os.environ["TEACHER_WEB__SITE_SUMMARY"])

    return render(request, "default/index.html", view_model.content)
