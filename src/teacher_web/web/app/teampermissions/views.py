import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.viewmodels.decorators.permissions import min_permission_required
from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from shared.models.core.django_helper import auth_user_id
from shared.models.enums.permissions import DEPARTMENT
from shared.view_model import ViewModel
from .viewmodels import TeamPermissionIndexViewModel, TeamPermissionEditViewModel, TeamPermissionDeleteViewModel

@permission_required('cssow.can_manage_team_permissions', login_url='/accounts/login')
@min_permission_required(DEPARTMENT.HEAD, login_url='/accounts/login')
def index(request):
    
    # TODO: #316 permissions_required decorator

    myTeamPermssionsViewModel = TeamPermissionIndexViewModel(db=db, request=request, auth_user=auth_user_id(request))
    
    return render(request, "teampermissions/index.html", myTeamPermssionsViewModel.view().content)    


@permission_required('cssow.can_manage_team_permissions', login_url='/accounts/login')
@min_permission_required(DEPARTMENT.HEAD, login_url='/accounts/login')
def edit(request, scheme_of_work_id, teacher_id):

    save_view = TeamPermissionEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_user_id(request))
    
    if request.method == "POST":
        save_view.execute()

        if save_view.saved == True:

            if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
                redirect_to_url = request.POST.get("next", None)
            else:
                redirect_to_url = reverse('team-permissions.index')
            return HttpResponseRedirect(redirect_to_url)
        
    return render(request, "teampermissions/edit.html", save_view.view().content)


@permission_required('cssow.can_manage_team_permissions', login_url='/accounts/login')
@min_permission_required(DEPARTMENT.ADMIN, login_url='/accounts/login')
def delete(request, scheme_of_work_id, teacher_id):
    
    """ delete item and redirect back to index """

    delete_viewmodel = TeamPermissionDeleteViewModel(db=db, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_user_id(request))
    delete_viewmodel.execute()

    return HttpResponseRedirect(reverse("team-permissions.index"))
