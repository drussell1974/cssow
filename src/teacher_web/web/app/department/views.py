from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.department.viewmodels import DepartmentAllViewModel, DepartmentEditViewModel, DepartmentIndexViewModel, DepartmentDeleteUnpublishedViewModel

# Create your views here.

@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator

    index_view =  DepartmentIndexViewModel(db=db, institute_id=institute_id, top=10, auth_user=auth_ctx)
    
    return render(request, "default/index.html", index_view.view(request).content)


@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def viewall(request, institute_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator

    all_view =  DepartmentAllViewModel(db=db, institute_id=institute_id, auth_user=auth_ctx)
    
    return render(request, "department/index.html", all_view.view(request).content)


@permission_required("cssow.change_institutemodel", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator

    save_view = DepartmentEditViewModel(db=db, request=request, auth_user=auth_ctx)
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse("institute.edit", args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "institute/edit.html", save_view.view(request).content)


@permission_required("cssow.delete_institutemodel", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    DepartmentDeleteUnpublishedViewModel(db=db, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("institute.index"))