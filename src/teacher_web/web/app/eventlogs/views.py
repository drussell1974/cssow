import os
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse
from shared.models.core.django_helper import auth_user_id

from shared.view_model import ViewModel
from .viewmodels import EventLogIndexViewModel

# Create your views here.


@permission_required('cssow.view_eventlogs', login_url='/accounts/login/')
def index(request):
    """ view the event log """    
    #raise Exception("search logs")
    modelview = EventLogIndexViewModel(db, request, auth_user=auth_user_id(request))
    
    return render(request, "eventlog/index.html", modelview.view().content)


def delete(request, days = 30):
    #TODO: #274 delete old logs
    raise NotImplementedError("delete view not implemented")