from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.enums.permissions import DEPARTMENT
from shared.models.decorators.permissions import min_permission_required
from shared.models.enums.publlished import STATE
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from ..lessons.viewmodels import LessonGetModelViewModel
from ..schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from ..department_topic.viewmodels import DepartmentTopicIndexViewModel, DepartmentTopicEditViewModel, DepartmentTopicDeleteUnpublishedViewModel #, LessonKS123PathwayGetModelViewModel, LessonKS123PathwaySaveViewModel, LessonKS123PathwayDeleteUnpublishedViewModel
from shared.models.core import validation_helper
from shared.view_model import ViewModel
from shared.wizard_helper import WizardHelper
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, auth_ctx):

    pathways_index = DepartmentTopicIndexViewModel(db, request, auth_ctx)

    return render(request, "department_topic/index.html", pathways_index.view(request).content)


#@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, topic_id = 0, auth_ctx = None):

    topic_edit = DepartmentTopicEditViewModel(db=db, request=request, topic_id=topic_id, auth_ctx=auth_ctx)
    if request.method == "POST":
        topic_edit.execute(published=STATE.PUBLISH)

        if topic_edit.saved:
            if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
                redirect_to_url = f"{request.POST.get('next', None)}#{topic_edit.model.id}"
            return HttpResponseRedirect(redirect_to_url)

    return render(request, "department_topic/edit.html", topic_edit.view(request).content)


#@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, auth_ctx):

    DepartmentTopicDeleteUnpublishedViewModel(db=db, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("department_topic.index", args=[institute_id, department_id]))
