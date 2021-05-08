import os
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.context import AuthCtx
from shared.models.decorators.permissions import min_permission_required
from django.db import connection as db
from django.urls import reverse_lazy
from django.views import generic
from shared.models.enums.permissions import DEPARTMENT
from shared.view_model import ViewModel
from .viewmodels import TeamPermissionIndexViewModel, TeamPermissionEditViewModel, TeamPermissionApproveViewModel, TeamPermissionDeleteViewModel, TeamPermissionRequestAccessViewModel, TeamPermissionRequestLoginViewModel

@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    myTeamPermssionsViewModel = TeamPermissionIndexViewModel(db=db, request=request, auth_user=auth_ctx)
    
    return render(request, "teampermissions/index.html", myTeamPermssionsViewModel.view(request).content)    


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, teacher_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    save_view = TeamPermissionEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_ctx, show_authorised=True)
    
    if request.method == "POST":
        save_view.execute()

        if save_view.saved == True:
            redirect_to_url = reverse('team-permissions.index', args=[institute_id, department_id])
            return HttpResponseRedirect(redirect_to_url)
       
    return render(request, "teampermissions/edit.html", save_view.view(request).content)


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.HEAD, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def approve(request, institute_id, department_id, scheme_of_work_id, teacher_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    approve_viewmodel = TeamPermissionApproveViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_ctx)
    approve_viewmodel.execute()

    return HttpResponseRedirect(reverse("team-permissions.index", args=[institute_id, department_id]))


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def reject(request, institute_id, department_id, scheme_of_work_id, teacher_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    reject_viewmodel = TeamPermissionDeleteViewModel(db=db, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_ctx)
    reject_viewmodel.execute()

    return HttpResponseRedirect(reverse("team-permissions.index", args=[institute_id, department_id]))


@permission_required('cssow.can_manage_team_permissions', login_url="/accounts/login")
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login", login_route_name="team-permissions.login-as")
def delete(request, institute_id, department_id, scheme_of_work_id, teacher_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    delete_viewmodel = TeamPermissionDeleteViewModel(db=db, scheme_of_work_id=scheme_of_work_id, teacher_id=teacher_id, auth_user=auth_ctx)
    delete_viewmodel.execute()

    return HttpResponseRedirect(reverse("team-permissions.index", args=[institute_id, department_id]))


@login_required
@min_permission_required(DEPARTMENT.NONE, login_url="/accounts/login")
def request_access(request, institute_id, department_id, scheme_of_work_id, permission, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    request_access_view = TeamPermissionRequestAccessViewModel(
        db=db,
        request=request, 
        scheme_of_work_id=scheme_of_work_id,
        teacher_name=auth_ctx.user_name,
        permission=permission,
        auth_user=auth_ctx)

    request_access_view.execute()
    
    # TODO: #490 notify head of department 

    uri = reverse("team-permissions.login-as", args=[institute_id, department_id, scheme_of_work_id, permission])
    next = request.GET['next']

    return HttpResponseRedirect(f"{uri}?next={next}")


class TeamPermissionRequestLoginView(auth_views.LoginView):
    ''' extend the LoginView to pass the scheme_of_work_id, permission and request_made to the login.html '''
    
    def get(self, request, *args, **kwargs):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, kwargs["institute_id"], kwargs["department_id"])
        
        func = super(TeamPermissionRequestLoginView, self).get_context_data
        
        request_login = TeamPermissionRequestLoginViewModel(db=db, request=request, get_context_data=func, auth_user=auth_ctx, **kwargs)
        
        return render(request, "registration/login.html", request_login.view(request))
