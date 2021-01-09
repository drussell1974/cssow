import os
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from shared.models.core.django_helper import auth_user_id
from shared.view_model import ViewModel
from .viewmodels import EventLogIndexViewModel, EventLogDeleteOldViewModel

# Create your views here.


@permission_required('cssow.view_eventlogs', login_url='/accounts/login/')
def index(request):
    """ view the event log """    
    modelview = EventLogIndexViewModel(db=db, request=request, settings=settings, auth_user=auth_user_id(request))
    
    return render(request, "eventlog/index.html", modelview.view().content)


@permission_required('cssow.delete_eventlogs', login_url='/accounts/login/')
def delete(request, rows = 0):
    """ delete old logs """
    modelview = EventLogDeleteOldViewModel(db=db, request=request, settings=settings, auth_user=auth_user_id(request))

    return render(request, "eventlog/index.html", modelview.view().content)
