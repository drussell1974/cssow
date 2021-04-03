from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.conf import settings
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.core import validation_helper
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import LESSON
from shared.models.decorators.permissions import min_permission_required
from shared.models.enums.publlished import STATE
from shared.wizard_helper import WizardHelper
from shared.view_model import ViewModel

from .viewmodels import LessonScheduleEditViewModel #, LessonPublishViewModel, LessonDeleteViewModel, LessonDeleteUnpublishedViewModel, LessonIndexViewModel, LessonWhiteboardViewModel, LessonMissingWordsChallengeViewModel, LessonGetModelViewModel

from datetime import datetime

# Create your views here.        
'''
@min_permission_required(LESSON.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, auth_ctx, lesson_id = 0):
    """ Get lessons for scheme of work """

    #367 get auth_ctx from min_permission_required decorator
    
    # default pager settings
    page = try_int(request.GET.get("page", 0))

    if page == 0:
        page = settings.PAGER["default"]["page"]
    
    pagesize = settings.PAGER["default"]["pagesize"]
    pagesize_options = settings.PAGER["default"]["pagesize_options"]
    keyword_search = request.POST.get("keyword_search", "")

    lessonIndexView = LessonIndexViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, page=page, pagesize=pagesize, pagesize_options=pagesize_options, keyword_search=keyword_search, auth_user=auth_ctx)

    return render(request, "lessons/index.html", lessonIndexView.view().content)
'''

@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, auth_ctx, lesson_id, schedule_id = 0):
    ''' Edit the lesson scheduule '''
    model = None
    
    modelview = LessonScheduleEditViewModel(db=db, request=request, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_ctx=auth_ctx)
        
    if request.method == "POST":
        ' saved the scheduled lesson '            
        modelview.execute()
        
        if modelview.saved == True:
            redirect_to_url = request.POST.get("next", None)
            return HttpResponseRedirect(redirect_to_url)
        else:
            handle_log_warning(db, model.id, "lesson schedule {} (id:{}) is invalid posting back to client - {}".format(model.class_code, model.id, model.validation_errors))
        
    return render(request, "lesson_schedules/edit.html", modelview.view().content)

'''
@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    # TODO: #367 get auth_ctx from min_permission_required decorator
    raise DeprecationWarning("remove if not longer in use")
    #367 get auth_ctx from min_permission_required decorator
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    LessonDeleteViewModel(db=db, auth_user=auth_ctx, lesson_id=lesson_id)

    return HttpResponseRedirect(redirect_to_url)
    

@min_permission_required(LESSON.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def whiteboard(request, institute_id, department_id,scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    #367 use min permissions NONE

    get_lesson_view =  LessonWhiteboardViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_lesson_view.model
    lesson_schedule = LessonScheduleModel.get_model(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    data = {
        "key_words":model.key_words,
        "learning_objectives":model.learning_objectives,
        "resources": model.resources,
        "lesson_schedule": lesson_schedule, 
        "STUDENT_WEB__WEB_SERVER_WWW": get_lesson_view.STUDENT_WEB__WEB_SERVER_WWW
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, ctx=auth_ctx, data=data)
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


@min_permission_required(LESSON.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def missing_words_challenge(request, institute_id, department_id,scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    #367 use min permissions NONE
        
    get_challenge_view =  LessonMissingWordsChallengeViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_challenge_view.model

    data = {
        "learning_objectives":model.learning_objectives,
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, ctx=auth_ctx, data=data)
    
    return render(request, "lessons/missing_words_view.html", view_model.content)
'''