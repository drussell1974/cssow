from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.models.core import validation_helper
from shared.models.core.log import handle_log_warning, handle_log_info

from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess
from shared.view_model import ViewModel

# TODO: use view models
from shared.models import cls_schemeofwork, cls_learningobjective

from shared.models.cls_lesson import LessonModel, LessonDataAccess
from shared.models.cls_ks123pathway import KS123PathwayDataAccess
from shared.models.cls_year import YearDataAccess
from shared.models.cls_topic import TopicDataAccess

# view models
from ..default.viewmodels import KeywordGetOptionsListViewModel
from .viewmodels import LessonSaveViewModel, LessonGetModelViewModel, LessonGetAllViewModel

from datetime import datetime

# Create your views here.        
def index(request, scheme_of_work_id):
    """ Get lessons for scheme of work """

    scheme_of_work_name = SchemeOfWorkDataAccess.get_schemeofwork_name_only(db, scheme_of_work_id)

    lessons_all = LessonGetAllViewModel(db, scheme_of_work_id, auth_user=request.user.id)
    schemeofwork_options = SchemeOfWorkDataAccess.get_options(db, auth_user=request.user.id)
    
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons_all.model,
        "topic_name": "",
    }

    view_model = ViewModel(scheme_of_work_name, scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)


@permission_required('cssow.add_lessonmodel', login_url='/accounts/login/')
def new(request, scheme_of_work_id):
    ''' Create a new lesson '''
    
    scheme_of_work = SchemeOfWorkDataAccess.get_model(db, scheme_of_work_id, request.user.id)
    
    get_lesson_view = LessonGetModelViewModel(db, 0, request.user.id)
    lesson = get_lesson_view.model

    lesson.key_stage_id = scheme_of_work.key_stage_id
    lesson.scheme_of_work_id = scheme_of_work.id
    year_options = YearDataAccess.get_options(db, scheme_of_work.key_stage_id)
    topic_options = TopicDataAccess.get_options(db, lvl=1)
    key_words = KeywordGetOptionsListViewModel(db).model

    data = {
        "scheme_of_work_id": int(scheme_of_work_id),
        "lesson_id": int(lesson.id),
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": 0, 
        "year_options": year_options,
        "selected_year_id": 0,
        "lesson": lesson,
        "key_words": key_words,
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "New", data=data)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, lesson_id):
    ''' Edit the lesson '''

    get_lesson_view = LessonGetModelViewModel(db, lesson_id, request.user.id)
    lesson = get_lesson_view.model

    scheme_of_work = SchemeOfWorkDataAccess.get_model(db, scheme_of_work_id, request.user.id)
    year_options = YearDataAccess.get_options(db, lesson.key_stage_id)
    topic_options = TopicDataAccess.get_options(db, lvl=1)
    key_words_options = KeywordGetOptionsListViewModel(db).model
    ks123_pathways = KS123PathwayDataAccess.get_options(db, lesson.year_id, lesson.topic_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson.id,
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": lesson.topic_id, 
        "year_options": year_options,
        "selected_year_id": lesson.year_id,
        "lesson": lesson,
        "key_words_options": key_words_options,
        "ks123_pathways": ks123_pathways,
        "show_ks123_pathway_selection": lesson.key_stage_id in (1,2,3)
    }
    
    #TODO: #231: pass the active model to ViewModel
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit: {}".format(lesson.title), data=data, active_model=lesson)
    
    return render(request, "lessons/edit.html", view_model.content)

    
@permission_required('cssow.add_lessonmodel', login_url='/accounts/login/')
def copy(request, scheme_of_work_id, lesson_id):
    ''' Copy the lesson '''
    get_lesson_view = LessonGetModelViewModel(db, lesson_id, request.user.id)
    lesson = get_lesson_view.model
    
    lesson.id = 0 # reset id

    scheme_of_work = SchemeOfWorkDataAccess.get_model(db, scheme_of_work_id, request.user.id)
    year_options = YearDataAccess.get_options(db, lesson.key_stage_id)
    topic_options = TopicDataAccess.get_options(db, lvl=1)
    key_words_options = KeywordGetOptionsListViewModel(db)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": 0,
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": lesson.topic_id, 
        "year_options": year_options,
        "selected_year_id": lesson.year_id,
        "lesson": lesson,
        "key_words_options": key_words_options,
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Copy: {}".format(lesson.title), data=data)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
def publish(request, scheme_of_work_id, lesson_id):
    ''' Publish the lesson '''
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    LessonDataAccess.publish(db, request.user.id, lesson_id)

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
def delete(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    LessonDataAccess.delete(db, request.user.id, lesson_id)

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


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id, lesson_id):
    """ save_item non-view action """
        
    published = int(request.POST["published"] if request.POST["published"] is not None else 1)
    
    model = LessonModel(
        id_ = request.POST["id"],
        orig_id = int(request.POST["orig_id"]),
        title = request.POST["title"],
        order_of_delivery_id = request.POST["order_of_delivery_id"],
        scheme_of_work_id = request.POST["scheme_of_work_id"],
        topic_id = request.POST["topic_id"],
        related_topic_ids = request.POST["related_topic_ids"],
        key_stage_id= request.POST.get("key_stage_id", 0),
        year_id = request.POST.get("year_id", 0),
        summary = request.POST["summary"],
        created = datetime.now(),
        created_by_id = request.user.id
    )

    model.pathway_ks123_ids = request.POST.getlist("pathway_ks123_ids")

    # reset id if a copy
    if int(request.POST["orig_id"]) > 0:
        model.id = int(request.POST["orig_id"])
        
    
    # TODO: Create viewmodel from serialized POST data https://www.django-rest-framework.org/api-guide/parsers/#formparser

    viewmodel = LessonSaveViewModel(db, model, key_words_json=request.POST.get("key_words"), auth_user=request.user.id)
    model = viewmodel.model
    
    model.validate()
    
    if model.is_valid == True:
        ' save the lesson '


        viewmodel.execute(published)
        model = viewmodel.model


        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """    
        handle_log_warning(db, "saving... lesson {} (id:{}) invalid - {}".format(model.title, model.id, model.validation_errors))

        request.session.alert_message = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id,lesson_id))
        

        scheme_of_work = SchemeOfWorkDataAccess.get_model(db, scheme_of_work_id, request.user.id)
        year_options = YearDataAccess.get_options(db, model.key_stage_id)
        topic_options = TopicDataAccess.get_options(db, lvl=1)
        key_words_options = KeywordGetOptionsListViewModel(db).model
        ks123_pathways = KS123DataAccess.get_options(db, model.year_id, model.topic_id)
        
        
        form_data = {
                "scheme_of_work_id": request.POST["scheme_of_work_id"],
                "lesson_id": request.POST["id"],
                "key_stage_id": request.POST.get("key_stage_id", 0),
                "topic_options": topic_options,
                "selected_topic_id": request.POST["topic_id"], 
                "year_options": year_options,
                "selected_year_id": request.POST.get("year_id", 0),
                "lesson": model, # lesson model
                "key_words_options": key_words_options,
                "ks123_pathways": ks123_pathways,
                "show_ks123_pathway_selection": model.key_stage_id in (1,2,3)
            }
            
        view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit: {} (Errors:{})".format(model.title, model.validation_errors), data=form_data)

        return render(request, "lessons/edit.html", view_model.content)
        
    return HttpResponseRedirect(redirect_to_url)


def initialise_keywords(request, scheme_of_work_id):
    
    raise DeprecationWarning("Not longer used.")

    lessons = LessonGetAllViewModel(db, scheme_of_work_id, auth_user=request.user.id)

    #for lesson in lessons.model:
    #   LessonDataAccess._upsert_key_words(db, lesson.model)

    #scheme_of_work_name = LessonDataAccess.get_schemeofwork_name_only(db, scheme_of_work_id)
    schemeofwork_options = LessonDataAccess.get_options(db, scheme_of_work_id, auth_user=request.user.id)
    
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

    LessonDataAccess.delete_unpublished(db, scheme_of_work_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)
