import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shared.models.core.context import Ctx
from shared.models.core.django_helper import auth_user_model
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from .viewmodels import EventLogIndexViewModel, EventLogDeleteOldViewModel

# Create your views here.


@permission_required('cssow.view_eventlogs', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url='/accounts/login/')
def index(request, institute_id, department_id, scheme_of_work_id):
    """ view the event log """ 
    
    view_ctx = Ctx(institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)
       
    modelview = EventLogIndexViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, settings=settings, auth_user=auth_ctx)
    
    return render(request, "eventlog/index.html", modelview.view().content)


@permission_required('cssow.delete_eventlogs', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url='/accounts/login/')
def delete(request, institute_id, department_id, scheme_of_work_id, rows = 0):
    """ delete old logs """

    view_ctx = Ctx(institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)
    
    modelview = EventLogDeleteOldViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, settings=settings, auth_user=auth_ctx)

    return render(request, "eventlog/index.html", modelview.view().content)
