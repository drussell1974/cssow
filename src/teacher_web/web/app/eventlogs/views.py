import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shared.models.core.context import AuthCtx
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from .viewmodels import EventLogIndexViewModel, EventLogDeleteOldViewModel

# Create your views here.


@permission_required('cssow.view_eventlogs', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url='/accounts/login/')
def index(request, institute_id, department_id, scheme_of_work_id, auth_ctx=None):

    # TODO: #367 get auth_ctx from min_permission_required decorator
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
       
    modelview = EventLogIndexViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, settings=settings, auth_user=auth_ctx)
    
    return render(request, "eventlog/index.html", modelview.view().content)


@permission_required('cssow.delete_eventlogs', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url='/accounts/login/')
def delete(request, institute_id, department_id, scheme_of_work_id, rows = 0, auth_ctx=None):

    # TODO: #367 get auth_ctx from min_permission_required decorator
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
    
    modelview = EventLogDeleteOldViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, settings=settings, auth_user=auth_ctx)

    return render(request, "eventlog/index.html", modelview.view().content)
