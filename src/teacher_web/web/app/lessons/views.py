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
from shared.models.cls_content import ContentModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_ks123pathway import KS123PathwayModel
from shared.models.cls_year import YearModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

from .viewmodels import LessonEditViewModel, LessonPublishViewModel, LessonDeleteViewModel, LessonDeleteUnpublishedViewModel, LessonIndexViewModel, LessonWhiteboardViewModel, LessonMissingWordsChallengeViewModel, LessonGetModelViewModel

from datetime import datetime

# Create your views here.        

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


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, auth_ctx, lesson_id = 0, is_copy = False):
    ''' Edit the lesson '''
    
    wizard = WizardHelper(
        add_another_url=reverse('lesson.new', args=[institute_id, department_id, scheme_of_work_id]),
        default_url=reverse('lesson.index', args=[auth_ctx.institute_id, auth_ctx.department_id, scheme_of_work_id])
    )
    
    # TODO: # use/create LessonEditViewModel
    #367 get auth_ctx from min_permission_required decorator
    
    model = LessonModel(id_=lesson_id, scheme_of_work_id=scheme_of_work_id)
    error_message = ""
    
    #253 check user id
    # TODO: #323 Use SchemeOfWorkContextModel.get_context_model(db, scheme_of_work_id, auth_ctx)
    # TODO: #323 SchemeOfWorkContextModel should return key_stage_id
    scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_ctx)

    lesson_schedule = None

    if request.method == "GET":
        ## GET request from client ##
        
        if lesson_id > 0:
            #253 check user id
            get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
            model = get_lesson_view.model  
            lesson_schedule = get_lesson_view.model.lesson_schedule      
            wizard.next_url=reverse('lesson_ks123pathways.select', args=[auth_ctx.institute_id, auth_ctx.department_id, scheme_of_work_id, lesson_id])

        # handle copy

        if is_copy == True:
            model.orig_id = lesson_id
            model.id = 0 # reset id
            model.title = "copy of " + model.title

        
    elif request.method == "POST":
        ## POST back from client ##
    
        published_state = STATE.parse(request.POST["published"] if request.POST["published"] is not None else "PUBLISH")
        
        model = LessonModel(
            id_ = request.POST["id"],
            orig_id = int(request.POST["orig_id"]),
            title = request.POST["title"],
            order_of_delivery_id = request.POST["order_of_delivery_id"],
            scheme_of_work_id = request.POST["scheme_of_work_id"],
            content_id = request.POST["content_id"],
            topic_id = request.POST["topic_id"],
            related_topic_ids = request.POST["related_topic_ids"],
            key_stage_id= scheme_of_work.key_stage_id,
            year_id = request.POST.get("year_id", 0),
            summary = request.POST["summary"],
            created = datetime.now(),
            #253 check user id
            created_by_id = auth_ctx.auth_user_id
        )

        model.pathway_ks123_ids = request.POST.getlist("pathway_ks123_ids")

        create_schedule = request.POST.get("generate_class_code", False)
        
        #253 check user id
        modelviewmodel = LessonEditViewModel(db=db, model=model, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx, create_schedule = create_schedule)

        try:
            modelviewmodel.execute(published_state)
            model = modelviewmodel.model
            lesson_schedule = modelviewmodel.lesson_schedule

            if model.is_valid == True:
                ' save the lesson '            
                # TODO: #386 determine wizard mode
                
                wizard.next_url=reverse('lesson_ks123pathways.select', args=[institute_id, department_id, scheme_of_work_id, modelviewmodel.model.id])
                
                redirect_to_url = wizard.get_redirect_url(request)

                return HttpResponseRedirect(redirect_to_url)
            
            else:
                handle_log_warning(db, scheme_of_work, "lesson {} (id:{}) is invalid posting back to client - {}".format(model.title, model.id, model.validation_errors))
        
        except Exception as e:
            error_message = e
    
    # render view
    
    #270 get ContentModel.get_options by scheme_of_work and key_stage_id
    content_options = ContentModel.get_options(db, scheme_of_work.key_stage_id, auth_ctx, scheme_of_work.id)
    topic_options = TopicModel.get_options(db, lvl=1, auth_user=auth_ctx)
    year_options = YearModel.get_options(db, key_stage_id=scheme_of_work.key_stage_id, auth_user=auth_ctx)
    ks123_pathways = KS123PathwayModel.get_options(db, scheme_of_work.key_stage_id, model.topic_id, auth_ctx)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "is_copy": is_copy,
        "key_stage_id": scheme_of_work.key_stage_id,
        "content_options": content_options,
        "topic_options": topic_options,
        "selected_topic_id": model.topic_id, 
        "year_options": year_options,
        "selected_year_id": model.year_id,
        "lesson": model,
        "ks123_pathways": ks123_pathways,
        "lesson_schedule": lesson_schedule
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit: {}".format(model.title) if model.id > 0 else "Create new lesson for %s" % scheme_of_work.name, ctx=auth_ctx, data=data, active_model=model, alert_message="", error_message=error_message, wizard=wizard)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish(request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    LessonPublishViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx, lesson_id=lesson_id)

    # check for null and 404

    # catch errors 500

    return HttpResponseRedirect(redirect_to_url)


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

    # TODO: Move to lesson_schedule.views

    get_lesson_view =  LessonWhiteboardViewModel(db=db, schedule_id=0, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_lesson_view.model
    lesson_schedule = LessonScheduleModel.get_model(db=db, schedule_id=0, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
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


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    LessonDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("lesson.index", args=[institute_id, department_id, scheme_of_work_id]))
