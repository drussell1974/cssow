import os
from django.shortcuts import render
from django.conf import settings
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from shared.models.decorators.permissions import min_permission_required
from shared.models.enums.permissions import DEPARTMENT
from shared.view_model import ViewModel
from .viewmodels import DefaultIndexViewModel

# Create your views here.
@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id=0, department_id=0, auth_ctx=None):

    #367 get auth_ctx from min_permission_required decorator
    
    modelview = DefaultIndexViewModel(db=db, top=5, auth_user=auth_ctx)
    
    view_model = modelview.view(settings.SITE_TITLE, settings.SITE_SUMMARY)

    return render(request, "default/index.html", view_model.content)


@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def academic_year(request, institute_id=0, department_id=0, auth_ctx=None):
    
    # change session
    if request.method == "POST":
        request.session["academic_year__selected_id"] = int(request.POST["academic_year"])
        
    # redirect back to page
    redirect_to_url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(redirect_to_url)
