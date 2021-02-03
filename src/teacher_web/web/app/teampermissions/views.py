import os
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.decorators.permissions import min_permission_required
from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from shared.models.core.django_helper import auth_user_id
from shared.models.enums.permissions import DEPARTMENT
from shared.view_model import ViewModel
from .viewmodels import TeamPermissionIndexViewModel, TeamPermissionEditViewModel, TeamPermissionDeleteViewModel, TeamPermissionRequestAccessViewModel, TeamPermissionRequestLoginViewModel

@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def index(request):
    
    # TODO: #316 permissions_required decorator

    myTeamPermssionsViewModel = TeamPermissionIndexViewModel(db=db, request=request, auth_user=auth_user_id(request))
    
    return render(request, "teampermissions/index.html", myTeamPermssionsViewModel.view().content)    


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login", login_route_name="team-permissions.login-as")
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


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def delete(request, scheme_of_work_id, teacher_id):
    
    """ delete item and redirect back to index """

    delete_viewmodel = TeamPermissionDeleteViewModel(db=db, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_user_id(request))
    delete_viewmodel.execute()

    return HttpResponseRedirect(reverse("team-permissions.index"))


@login_required
def request_access(request, scheme_of_work_id, permission):

    request_access_view = TeamPermissionRequestAccessViewModel(
        db=db,
        request=request, 
        scheme_of_work_id=scheme_of_work_id, 
        teacher_id = request.user.id, 
        teacher_name=request.user.get_username(),
        permission=permission,
        auth_user=auth_user_id(request))

    request_access_view.execute()
    
    uri = reverse("team-permissions.login-as", args=[scheme_of_work_id, permission])
    next = request.GET['next']

    return HttpResponseRedirect(f"{uri}?next={next}")


class TeamPermissionRequestLoginView(auth_views.LoginView):
    ''' extend the LoginView to pass the scheme_of_work_id, permission and request_made to the login.html '''
    
    def get(self, request, *args, **kwargs):
        ''' override the get function '''
        
        func =super(TeamPermissionRequestLoginView, self).get_context_data

        request_login = TeamPermissionRequestLoginViewModel(db=db, request=request, get_context_data=func, auth_user=auth_user_id(request), **kwargs)
        
        return render(request, "registration/login.html", request_login.view())

