from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.models.core.log_handlers import handle_log_warning
from shared.models.core.django_helper import auth_user_model
# TODO: remove after creating view model
from shared.view_model import ViewModel
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from .viewmodels import ContentIndexViewModel, ContentEditViewModel, ContentDeleteUnpublishedViewModel
from shared.models.cls_content import ContentModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel


@min_permission_required(SCHEMEOFWORK.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, scheme_of_work_id):

    #253 check user id
    view_model = ContentIndexViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))
    
    return render(request, "content/index.html", view_model.view().content)


#234 add permission
@permission_required('models.change_contentmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, scheme_of_work_id, content_id=0):
    """ edit curriculum content """

    #253 check user id
    view_model = ContentEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, content_id=content_id, auth_user=auth_user_model(db, request))

    if view_model.is_content_ready:
        
        redirect_to_url = reverse('content.index', args=[scheme_of_work_id])

        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        
        return HttpResponseRedirect(redirect_to_url)


    return render(request, "content/edit.html", view_model.view().content)    


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, scheme_of_work_id):
    """ delete item and redirect back to referer """

    ContentDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))

    return HttpResponseRedirect(reverse("content.index", args=[scheme_of_work_id]))
