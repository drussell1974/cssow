from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.models.enums.publlished import STATE
from shared.view_model import ViewModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from ..lessons.viewmodels import LessonGetModelViewModel
from ..schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from ..lesson_keywords.viewmodels import LessonKeywordGetModelViewModel, LessonKeywordIndexViewModel, LessonKeywordSelectViewModel, LessonKeywordSaveViewModel, LessonKeywordDeleteUnpublishedViewModel
from shared.models.core import validation_helper
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

@min_permission_required(SCHEMEOFWORK.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    getall_keywords = LessonKeywordIndexViewModel(db=db, request=request, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)  
    
    return render(request, "lesson_keywords/index.html", getall_keywords.view(request).content)


# 299 Keyword Index
@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def select(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    keywords_select = LessonKeywordSelectViewModel(db=db, request=request, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)  
    
    if request.method == "POST":
        
        keywords_select.execute(request)
    
        if keywords_select.saved == True:
            if request.POST["next"] != "None" and request.POST["next"] != "":        
                redirect_to_url = request.POST["next"]
                return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "lesson_keywords/select.html", keywords_select.view(request).content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def new(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    model = KeywordModel(
        id_=0,
        term="",
        definition="",
        scheme_of_work_id=scheme_of_work_id)
    
    model.belongs_to_lessons.append(lesson_id)

    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    lesson = get_lesson_view.model

    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "keyword": model
    }
    
    view_model = ViewModel(lesson.title, lesson.title, "Create new keyword for %s" % lesson.title, ctx=auth_ctx, data=data)
    
    return render(request, "lesson_keywords/edit.html", view_model.content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    get_model_view = LessonKeywordGetModelViewModel(db=db, keyword_id=keyword_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_model_view.model
    
    if model == None:
        model = KeywordModel(
            id_=0,
            term="",
            definition="",
            scheme_of_work_id=scheme_of_work_id)
        
    model.belongs_to_lessons.append(lesson_id)

    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)    
    lesson = get_lesson_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "keyword_id": model.id,
        "keyword": model,
    }

    #231: pass the active model to ViewModel
    view_model = ViewModel(lesson.title, lesson.title, "Edit: {} for {}".format(model.term, lesson.title), ctx=auth_ctx, data=data, active_model=model, alert_message="")

    return render(request, "lesson_keywords/edit.html", view_model.content)


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


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    KeywordModel.delete(db, keyword_id, lesson_id=lesson_id, auth_user=auth_ctx)

    return HttpResponseRedirect(redirect_to_url)


@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id, auth_ctx):
    
    #367 get auth_ctx from min_permission_required decorator
    
    KeywordModel.publish_by_id(db, keyword_id, auth_ctx)

    return HttpResponseRedirect(reverse("lesson_keywords.index", args=[institute_id, department_id, scheme_of_work_id, lesson_id]))


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    LessonKeywordDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("lesson_keywords.index", args=[institute_id, department_id, scheme_of_work_id, lesson_id]))
