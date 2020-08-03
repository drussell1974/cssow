from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from shared.models.core import validation_helper
from shared.models.core.log import handle_log_warning, handle_log_info
from shared.view_model import ViewModel
# view models
from shared.models.cls_lesson import LessonModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_ks123pathway import KS123PathwayModel
from shared.models.cls_year import YearModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

from .viewmodels import LessonEditViewModel, LessonPublishViewModel, LessonDeleteViewModel, LessonDeleteUnpublishedViewModel, LessonIndexViewModel, LessonGetModelViewModel

from datetime import datetime

# Create your views here.        
def index(request, scheme_of_work_id):
    """ Get lessons for scheme of work """
    
    lessonIndexView = LessonIndexViewModel(db, scheme_of_work_id, auth_user=request.user.id)

    scheme_of_work_name = SchemeOfWorkModel.get_schemeofwork_name_only(db, scheme_of_work_id)

    schemeofwork_options = SchemeOfWorkModel.get_options(db, auth_user=request.user.id)
    
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessonIndexView.model,
        "topic_name": "",
    }

    view_model = ViewModel(scheme_of_work_name, scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, lesson_id = 0, is_copy = False):
    ''' Edit the lesson '''
    model = LessonModel(id_=lesson_id, scheme_of_work_id=scheme_of_work_id)
    scheme_of_work = SchemeOfWorkModel.get_by_id(db, scheme_of_work_id, request.user.id)
    
    if request.method == "GET":
        ## GET request from client ##
        
        get_lesson_view = LessonGetModelViewModel(db, lesson_id, request.user.id)
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
            topic_id = request.POST["topic_id"],
            related_topic_ids = request.POST["related_topic_ids"],
            key_stage_id= scheme_of_work.key_stage_id,
            year_id = request.POST.get("year_id", 0),
            summary = request.POST["summary"],
            created = datetime.now(),
            created_by_id = request.user.id
        )

        model.pathway_ks123_ids = request.POST.getlist("pathway_ks123_ids")

        viewmodel = LessonEditViewModel(db, model, key_words_json=request.POST.get("key_words"), auth_user=request.user.id)

        viewmodel.execute(published)
        model = viewmodel.model
        
        if model.is_valid == True:
            ' save the lesson '            
            redirect_to_url = ""

            if request.POST["next"] != "None"  and request.POST["next"] != "":
                redirect_to_url = request.POST["next"]
                            
            redirect_to_url = reverse('lesson.index', args=[model.scheme_of_work_id])
            return HttpResponseRedirect(redirect_to_url)
        else:
            handle_log_warning(db, "lesson {} (id:{}) is invalid posting back to client - {}".format(model.title, model.id, model.validation_errors))
            
    # render view
    
    topic_options = TopicModel.get_options(db, lvl=1)
    key_words_options = KeywordModel.get_options(db)
    year_options = YearModel.get_options(db, key_stage_id=scheme_of_work.key_stage_id)
    ks123_pathways = KS123PathwayModel.get_options(db, model.year_id, model.topic_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "is_copy": is_copy,
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": model.topic_id, 
        "year_options": year_options,
        "selected_year_id": model.year_id,
        "lesson": model,
        "key_words_options": key_words_options,
        "ks123_pathways": ks123_pathways,
        "show_ks123_pathway_selection": model.key_stage_id in (1,2,3)
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit: {}".format(model.title) if model.id > 0 else "New", data=data, active_model=model)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
def publish(request, scheme_of_work_id, lesson_id):
    ''' Publish the lesson '''
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    publishlesson_view = LessonPublishViewModel(db, request.user.id, lesson_id)

    # check for null and 404

    # catch errors 500

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
def delete(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    viewmodel = LessonDeleteViewModel(db, request.user.id, lesson_id)

    return HttpResponseRedirect(redirect_to_url)
    
    
def lessonplan(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan '''

    scheme_of_work_name = "" # TODO: get scheme of work name
    lesson_name = "" # TODO: get lesson name

    view_model = ViewModel(scheme_of_work_name, lesson_name, "lesson plan")
    
    return render(request, "lessons/lessonplan.html", view_model.content)

    
def whiteboard(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan on the whiteboard '''

    get_lesson_view =  LessonGetModelViewModel(db, lesson_id, request.user.id)
    model = get_lesson_view.model

    data = {
        "key_words":model.key_words,
        "learning_objectives":model.learning_objectives,
        "resources": model.resources,
    }

    view_model = ViewModel(model.title, model.title, model.topic_name, data=data)
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


def initialise_keywords(request, scheme_of_work_id):
    
    raise DeprecationWarning("Not longer used.")

    lessons = LessonIndexViewModel(db, scheme_of_work_id, auth_user=request.user.id)

    #for lesson in lessons.model:
    #    LessonModel._upsert_key_words(db, lesson.model)

    scheme_of_work_name = SchemeOfWorkModel.get_schemeofwork_name_only(db, scheme_of_work_id)
    schemeofwork_options = LessonModel.get_options(db, scheme_of_work_id, auth_user=request.user.id)
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("scheme_of_work_name", "scheme_of_work_name", "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
def delete_unpublished(request, scheme_of_work_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    #235 Create ViewModel
    LessonDeleteUnpublishedViewModel(db, scheme_of_work_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)
