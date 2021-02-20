from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.conf import settings
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.core import validation_helper
from shared.models.core.context import AuthCtx
from shared.models.core.log_handlers import handle_log_warning, handle_log_info
from shared.models.enums.permissions import LESSON
from shared.models.decorators.permissions import min_permission_required, unauthorise_request
from shared.view_model import ViewModel
from shared.models.cls_lesson import LessonModel, try_int
from shared.models.cls_content import ContentModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_ks123pathway import KS123PathwayModel
from shared.models.cls_year import YearModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

from .viewmodels import LessonEditViewModel, LessonPublishViewModel, LessonDeleteViewModel, LessonDeleteUnpublishedViewModel, LessonIndexViewModel, LessonWhiteboardViewModel, LessonGetModelViewModel

from datetime import datetime

# Create your views here.        

@min_permission_required(LESSON.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, lesson_id = 0):
    """ Get lessons for scheme of work """

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
    
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
def edit(request, institute_id, department_id, scheme_of_work_id, lesson_id = 0, is_copy = False):
    ''' Edit the lesson '''
    
    # TODO: # use/create LessonEditViewModel
    
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
    
    model = LessonModel(id_=lesson_id, scheme_of_work_id=scheme_of_work_id)
    error_message = ""
    
    #253 check user id
    scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_ctx)

    if request.method == "GET":
        ## GET request from client ##
        
        if lesson_id > 0:
            #253 check user id
            get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
            model = get_lesson_view.model
    
        # handle copy

        if is_copy == True:
            model.orig_id = lesson_id
            model.id = 0 # reset id
            model.title = "copy of " + model.title

            
    elif request.method == "POST":
        ## POST back from client ##
        
        published = int(request.POST["published"] if request.POST["published"] is not None else 1)
        
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

        #253 check user id
        modelviewmodel = LessonEditViewModel(db=db, model=model, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

        try:
            modelviewmodel.execute(published)
            model = modelviewmodel.model
        

            if model.is_valid == True:
                ' save the lesson '            
                redirect_to_url = reverse('lesson.index', args=[auth_ctx.institute_id, auth_ctx.department_id, model.scheme_of_work_id])
                
                if request.POST["next"] != "None"  and request.POST["next"] != "":
                    redirect_to_url = request.POST["next"]
                
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
    ks123_pathways = KS123PathwayModel.get_options(db, model.year_id, model.topic_id, auth_ctx)
    
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
        "show_ks123_pathway_selection": model.key_stage_id in (1,2,3)
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit: {}".format(model.title) if model.id > 0 else "Create new lesson for %s" % scheme_of_work.name, ctx=auth_ctx, data=data, active_model=model, alert_message="", error_message=error_message)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish(request, institute_id, department_id, scheme_of_work_id, lesson_id):
    ''' Publish the lesson '''
    
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    LessonPublishViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx, lesson_id=lesson_id)

    # check for null and 404

    # catch errors 500

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete(request, institute_id, department_id, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    raise DeprecationWarning("remove if not longer in use")

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    LessonDeleteViewModel(db=db, auth_user=auth_ctx, lesson_id=lesson_id)

    return HttpResponseRedirect(redirect_to_url)
    

@unauthorise_request
def whiteboard(request, institute_id, department_id,scheme_of_work_id, lesson_id):
    ''' Display the lesson plan on the whiteboard '''

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    #253 check user id
    get_lesson_view =  LessonWhiteboardViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_lesson_view.model

    data = {
        "key_words":model.key_words,
        "learning_objectives":model.learning_objectives,
        "resources": model.resources,
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, ctx=auth_ctx, data=data)
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id):
    """ delete item and redirect back to referer """

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    LessonDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("lesson.index", args=[institute_id, department_id, scheme_of_work_id]))
