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
from ..ks123pathways.viewmodels import KS123PathwayIndexViewModel #, LessonKS123PathwayGetModelViewModel, LessonKS123PathwaySaveViewModel, LessonKS123PathwayDeleteUnpublishedViewModel
from shared.models.core import validation_helper
from shared.view_model import ViewModel
from shared.wizard_helper import WizardHelper
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

#@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, auth_ctx):

    pathways_index = KS123PathwayIndexViewModel(db, request, auth_ctx)

    return render(request, "ks123pathway/index.html", pathways_index.view().content)


#@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, auth_ctx):

    raise NotImplementedError("not supported")

    return render(request, "ks123pathway/edit.html")

'''
@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def save(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id, auth_ctx):

    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
     
    #367 get auth_ctx from min_permission_required decorator

    error_message = ""

    """ save_item non-view action """
    
    published_state = STATE.parse(request.POST.get("published", "DRAFT"))

    model = KeywordModel(
        id_=keyword_id,
        scheme_of_work_id=scheme_of_work_id,
        term=request.POST.get("term", ""),
        definition=request.POST.get("definition", ""),
        created=datetime.now(),
        #253 check user id
        created_by_id=auth_ctx,
        published=published_state
    )
    # 299 must ensure other lessons are not deleted during save
    model.belongs_to_lessons.append(lesson_id)

    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    save_keyword_view = LessonKeywordSaveViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, model=model, auth_user=auth_ctx)
    
    save_keyword_view.execute(published_state)

    model = save_keyword_view.model
    

    if model.is_valid == True:
        ' saved keyword '
  
        ' redirect as necessary '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('keyword.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """

        #253 check user id
        get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)    
        lesson = get_lesson_view.model
        
        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "lesson_id": lesson_id,
            "keyword_id": model.id,
            "keyword": model,
        }

        # determine heading
        sub_heading = "Create new keyword for {}".format(lesson.title)
        if model.id > 0:
            sub_heading = "Edit: {} for {}".format(model.term, lesson.title)

        view_model = ViewModel(lesson.title, lesson.title, sub_heading, ctx=auth_ctx, data=data, active_model=model, alert_message="", error_message=error_message)
    
        return render(request, "lesson_keywords/edit.html", view_model.content)

    return HttpResponseRedirect(redirect_to_url)
'''

#@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, auth_ctx):

    raise NotImplementedError("not supported")

    #LessonKeywordDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("ks123pathway.index", args=[institute_id, department_id]))