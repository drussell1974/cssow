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
from shared.models.cls_lesson import LessonModel, try_int
from shared.models.cls_lesson_schedule import LessonScheduleModel


#from .viewmodels import LessonScheduleEditViewModel #, LessonPublishViewModel, LessonDeleteViewModel, LessonDeleteUnpublishedViewModel, LessonIndexViewModel, LessonWhiteboardViewModel, LessonMissingWordsChallengeViewModel, LessonGetModelViewModel

from datetime import datetime

# Create your views here.        

@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, auth_ctx, lesson_id, schedule_id = 0):
    ''' Edit the lesson scheduule '''
    
    return render(request, "lesson_schedules/edit.html")
