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
from .viewmodels import LessonScheduleIndexViewModel, LessonScheduleEditViewModel, LessonScheduleDeleteViewModel, LessonScheduleWhiteboardViewModel 
from datetime import datetime

# Create your views here.        

@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):
    """ Get schedules for lesson """
    
    scheduleIndexView = LessonScheduleIndexViewModel(db=db, request=request, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    return render(request, "lesson_schedules/index.html", scheduleIndexView.view().content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, auth_ctx, lesson_id, schedule_id = 0):
    ''' Edit the lesson scheduule '''
    model = None
    
    #432 create url for notification
    ''' creates url from lesson index e.g. /institute/2/department/5/schemesofwork/11/lessons#220 '''
    action_url =  f"{reverse('lesson_schedule.index', args=[institute_id, department_id, scheme_of_work_id, lesson_id])}#{schedule_id}"
    
    modelview = LessonScheduleEditViewModel(db=db, request=request, action_url=action_url, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_ctx=auth_ctx)
        
    if request.method == "POST":
        ' saved the scheduled lesson '            
        modelview.execute()
        
        if modelview.saved == True:
            redirect_to_url = request.POST.get("next", None)
            return HttpResponseRedirect(redirect_to_url)
        else:
            handle_log_warning(db, model.id, "lesson schedule {} (id:{}) is invalid posting back to client - {}".format(model.class_code, model.id, model.validation_errors))
        
    return render(request, "lesson_schedules/edit.html", modelview.view().content)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete(request, institute_id, department_id, scheme_of_work_id, lesson_id, schedule_id, auth_ctx):

    redirect_to_url = request.META.get('HTTP_REFERER')

    delete_view = LessonScheduleDeleteViewModel(db=db, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_ctx=auth_ctx)
    delete_view.execute()

    return HttpResponseRedirect(f"{redirect_to_url}#{lesson_id}")
    

@min_permission_required(LESSON.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def whiteboard(request, institute_id, department_id, scheme_of_work_id, lesson_id, schedule_id, auth_ctx):

    get_lesson_view =  LessonScheduleWhiteboardViewModel(db=db, schedule_id=schedule_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_lesson_view.model
    
    data = {
        "key_words":model.key_words,
        "learning_objectives":model.learning_objectives,
        "resources": model.resources,
        "lesson_schedule": get_lesson_view.lesson_schedule, 
        "STUDENT_WEB__WEB_SERVER_WWW": get_lesson_view.STUDENT_WEB__WEB_SERVER_WWW
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, ctx=auth_ctx, data=data)
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


@min_permission_required(LESSON.NONE, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def missing_words_challenge(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):
 
    get_challenge_view =  LessonMissingWordsChallengeViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_challenge_view.model

    data = {
        "learning_objectives":model.learning_objectives,
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, ctx=auth_ctx, data=data)
    
    return render(request, "lessons/missing_words_view.html", view_model.content)

