from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.institute.viewmodels import InstituteEditViewModel
from app.institute.viewmodels import InstituteIndexViewModel, InstituteAllViewModel
from app.institute.viewmodels import InstituteDeleteUnpublishedViewModel

# Create your views here.

@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, auth_ctx):
    
    index_view =  InstituteIndexViewModel(db=db, top=10, auth_user=auth_ctx)
    
    return render(request, "default/index.html", index_view.view("Schemes of Work", "Institutes").content)


@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def all(request, auth_ctx):
    
    all_view =  InstituteAllViewModel(db=db, auth_user=auth_ctx)
    
    return render(request, "institute/index.html", all_view.view().content)


@permission_required("cssow.change_institutemodel", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, auth_ctx):
    
    save_view = InstituteEditViewModel(db=db, request=request, auth_user=auth_ctx)
    
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse("institute.edit", args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "institute/edit.html", save_view.view().content)


@permission_required("cssow.delete_institutemodel", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, auth_ctx):

    InstituteDeleteUnpublishedViewModel(db=db, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("institute.index"))