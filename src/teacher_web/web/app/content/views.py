from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.models.core.log import handle_log_warning
from shared.models.core.django_helper import auth_user_id

# TODO: remove after creating view model
from shared.view_model import ViewModel
from .viewmodels import ContentIndexViewModel, ContentEditViewModel

from shared.models.cls_content import ContentModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

def index(request, scheme_of_work_id):

    #253 check user id
    view_model = ContentIndexViewModel(db, scheme_of_work_id, auth_user_id(request))
    
    return render(request, "content/index.html", view_model.view().content)


#234 add permission
@permission_required('models.change_contentmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, content_id=0):
    """ edit curriculum content """

    #253 check user id
    view_model = ContentEditViewModel(db, request, scheme_of_work_id, content_id, auth_user_id(request))

    if view_model.is_content_ready:
        
        redirect_to_url = reverse('content.index', args=[scheme_of_work_id])

        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        
        return HttpResponseRedirect(redirect_to_url)


    return render(request, "content/edit.html", view_model.view().content)    