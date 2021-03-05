import os
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse
from shared.models.core.context import AuthCtx
from shared.view_model import ViewModel
from .viewmodels import DefaultIndexViewModel

# Create your views here.
def index(request):

    auth_ctx = AuthCtx(db, request, 0, 0)
    
    # get the schemes of work
    #253 check user id
    modelview = DefaultIndexViewModel(db=db, top=5, auth_user=auth_ctx)
    
    view_model = modelview.view(os.environ["TEACHER_WEB__SITE_TITLE"], os.environ["TEACHER_WEB__SITE_SUMMARY"])

    return render(request, "default/index.html", view_model.content)

