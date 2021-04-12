from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.academic_years.viewmodels import AcademicYearIndexViewModel, AcademicYearEditViewModel #, DepartmentIndexViewModel, DepartmentDeleteUnpublishedViewModel

# Create your views here.

@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator

    index_view =  AcademicYearIndexViewModel(db=db, institute_id=institute_id, auth_user=auth_ctx)
    
    return render(request, "default/index.html", index_view.view(index_view.institute.name, "Academic Years").content)


@permission_required("cssow.change_institutemodel", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, year, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator

    save_view = AcademicYearEditViewModel(db=db, request=request, year=year, auth_user=auth_ctx)
    
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse("institute.edit", args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "academic_year/edit.html", save_view.view().content)
