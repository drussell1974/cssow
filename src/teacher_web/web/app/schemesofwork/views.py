from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.context import Ctx
from shared.models.core.django_helper import auth_user_model
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkIndexViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkDeleteUnpublishedViewModel

# Create your views here.

def index(request, institute_id, department_id):
    """ show schemes of work """
    
    view_ctx = Ctx(institute_id=institute_id, department_id=department_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)
    
    index_view =  SchemeOfWorkIndexViewModel(db=db, auth_user=auth_user_model(db, request, ctx=auth_ctx))
    
    return render(request, "schemesofwork/index.html", index_view.view().content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id = 0):
    """ edit action """
    view_ctx = Ctx(institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)
    
    save_view = SchemeOfWorkEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse('schemesofwork.edit', args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "schemesofwork/edit.html", save_view.view().content)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id):
    """ delete item and redirect back to referer """
    view_ctx = Ctx(institute_id=institute_id, department_id=department_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)

    SchemeOfWorkDeleteUnpublishedViewModel(db=db, auth_user=auth_user_model(db, request, ctx=auth_ctx))

    return HttpResponseRedirect(reverse("schemesofwork.index", args=[institute_id, department_id]))