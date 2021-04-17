from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.wizard_helper import WizardHelper
from shared.view_model import ViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel, SchemeOfWorkIndexViewModel, SchemeOfWorkDeleteUnpublishedViewModel
# Create your views here.

@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    index_view =  SchemeOfWorkIndexViewModel(db=db, auth_user=auth_ctx)
    
    return render(request, "schemesofwork/index.html", index_view.view().content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, auth_ctx, scheme_of_work_id = 0):

    wizard = WizardHelper(
        default_url=reverse('schemesofwork.index', args=[institute_id, department_id]),
        add_another_url=reverse('schemesofwork.new', args=[institute_id, department_id])
    )

    if scheme_of_work_id > 0:
        wizard.next_url=reverse('content.new', args=[institute_id, department_id, scheme_of_work_id])
        
    save_view = SchemeOfWorkEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx, wizard=wizard)
    
    if save_view.saved == True:
        
        # TODO: #386 determine wizard mode
        
        wizard.next_url=reverse('content.new', args=[institute_id, department_id, save_view.model.id])
        
        redirect_to_url = wizard.get_redirect_url(request)

        return HttpResponseRedirect(redirect_to_url)
    return render(request, "schemesofwork/edit.html", save_view.view().content)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    SchemeOfWorkDeleteUnpublishedViewModel(db=db, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("schemesofwork.index", args=[institute_id, department_id]))

'''
@permission_required("cssow.view_schedule", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def schedule(request, institute_id, department_id, scheme_of_work_id, auth_ctx):    
    
    schedule_view =  SchemeOfWorkScheduleViewModel(db=db, request=request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    if request.method == "POST":
        lesson_id = int(request.POST.get("lesson_id", 0))
        start_date_str = request.POST.get("start_date")
        return_to_url = request.META.get('HTTP_REFERER')
        redirect_to_url = f"{reverse('lesson_schedule.new', args=[institute_id, department_id, scheme_of_work_id, lesson_id])}?start_date={start_date_str}&redirect_to_url={return_to_url}"

        return HttpResponseRedirect(redirect_to_url)


    sub_heading = "Scheduled lessons"

    return render(request, "schemesofwork/schedule.html", schedule_view.view(schedule_view.scheme_of_work.name, sub_heading).content)

'''