from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.models.core.log import handle_log_warning

# TODO: remove after creating view model
from shared.view_model import ViewModel
from .viewmodels import ContentIndexViewModel, ContentEditViewModel

from shared.models.cls_content import ContentModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

def index(request, scheme_of_work_id):

    view_model = ContentIndexViewModel(db, scheme_of_work_id, request.user.id)
    
    return render(request, "content/index.html", view_model.view().content)


def edit(request, scheme_of_work_id, content_id=0):

    view_model = ContentEditViewModel(db, request, scheme_of_work_id, content_id, request.user.id)

    if view_model.is_content_ready:
        
        redirect_to_url = reverse('content.index', args=[scheme_of_work_id])

        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        
        return HttpResponseRedirect(redirect_to_url)


    return render(request, "content/edit.html", view_model.view().content)    