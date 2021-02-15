from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.context import AuthCtx
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.department.viewmodels import DepartmentEditViewModel
from app.department.viewmodels import DepartmentIndexViewModel
from app.department.viewmodels import DepartmentDeleteUnpublishedViewModel

# Create your views here.

def index(request, institute_id):
    #253 check user id
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=0)
    
    getall_view =  DepartmentIndexViewModel(db=db, institute_id=institute_id, auth_user=auth_ctx)
    
    return render(request, "department/index.html", getall_view.view().content)


@permission_required('cssow.change_institutemodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id):
    """ edit action """
    
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id)

    save_view = DepartmentEditViewModel(db=db, request=request, auth_user=auth_ctx)
    
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse('institute.edit', args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "institute/edit.html", save_view.view().content)


@permission_required('cssow.delete_institutemodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id):
    """ delete item and redirect back to referer """

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=0)

    DepartmentDeleteUnpublishedViewModel(db=db, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("institute.index"))