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
from .viewmodels import SchemeOfWorkScheduleIndexViewModel

# Create your views here.

@permission_required("cssow.view_schedule", login_url="/accounts/login/")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, auth_ctx):    
    
    schedule_view =  SchemeOfWorkScheduleIndexViewModel(db=db, request=request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    if request.method == "POST":
        lesson_id = int(request.POST.get("lesson_id", 0))
        start_date_str = request.POST.get("start_date")
        return_url = request.path # return to this page
        redirect_to_url = f"{reverse('lesson_schedule.new', args=[institute_id, department_id, scheme_of_work_id, lesson_id])}?start_date={start_date_str}&return_url={return_url}"

        return HttpResponseRedirect(redirect_to_url)


    sub_heading = "Scheduled lessons"

    return render(request, "schemesofwork/schedule.html", schedule_view.view(schedule_view.scheme_of_work.name, sub_heading).content)
