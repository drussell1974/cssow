from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel

from .viewmodels import LearningObjectiveSaveViewModel
from .viewmodels import LearningObjectiveGetModelViewModel
from .viewmodels import LearningObjectiveIndexViewModel
from .viewmodels import LearningObjectiveDeleteUnpublishedViewModel
from .viewmodels import LearningObjectivePublishModelViewModel

#from app.lessons.viewmodels import LessonGetOptionsViewModel

# TODO: use in view models
from shared.models.cls_lesson import LessonModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_solotaxonomy import SoloTaxonomyModel
from shared.models.cls_content import ContentModel
from shared.models.cls_examboard import ExamBoardModel

from shared.models.core import validation_helper

# view models
from app.lessons.viewmodels import LessonGetModelViewModel


def index(request, scheme_of_work_id, lesson_id):
    ''' Get learning objectives for lesson '''

    get_lesson_view = LessonGetModelViewModel(db, lesson_id, scheme_of_work_id, request.user.id)
    lesson = get_lesson_view.model

    learningobjectives_view = LearningObjectiveIndexViewModel(db, lesson_id, scheme_of_work_id, request.user.id)
    
    lesson_options = LessonModel.get_options(db, scheme_of_work_id, request.user.id)  
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "lesson_id":int(lesson_id),
        "lesson": lesson,
        "learning_objectives": learningobjectives_view.model,
        "lesson_options": lesson_options,
    }

    view_model = ViewModel("", lesson.title, lesson.summary, data=data)
    
    return render(request, "learningobjectives/index.html", view_model.content)


@permission_required('cssow.add_learningobjectivemodel', login_url='/accounts/login/')
def new(request, scheme_of_work_id, lesson_id):
    ''' Create a new learning objective '''

    # check if an existing_learning_objective_id has been passed
     
    get_lessonobjective_view = LearningObjectiveGetModelViewModel(db, 0, scheme_of_work_id, lesson_id, request.user.id)
    model = get_lessonobjective_view.model
    
    get_lesson_view = LessonGetModelViewModel(db, int(lesson_id), scheme_of_work_id, request.user.id)
    lesson = get_lesson_view.model

    if scheme_of_work_id is not None:
        # required for creating a new object
        get_lessonobjective_view.model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        get_lessonobjective_view.model.lesson_id = int(lesson_id)

    key_stage_id = SchemeOfWorkModel.get_key_stage_id_only(db, int(scheme_of_work_id))

    get_lessonobjective_view.model.lesson_id = lesson.id
    get_lessonobjective_view.model.key_stage_id = key_stage_id

    solo_taxonomy_options = SoloTaxonomyModel.get_options(db)

    content_options = ContentModel.get_options(db, key_stage_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": 0,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    
    view_model = ViewModel("", lesson.title, "New", data=data)
    
    return render(request, "learningobjectives/edit.html", view_model.content)


@permission_required('cssow.change_learningobjectivemodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, lesson_id, learning_objective_id):
    ''' Edit an existing learning objective '''
    
    get_model_viewmodel = LearningObjectiveGetModelViewModel(db, learning_objective_id, lesson_id, scheme_of_work_id, request.user.id)
    model = get_model_viewmodel.model

    # redirect if not found
    if model is None or model.id == 0:
        redirect_to_url = reverse("learningobjective.index", args=[scheme_of_work_id, lesson_id])
        return HttpResponseRedirect(redirect_to_url)


    get_lesson_view = LessonGetModelViewModel(db, int(lesson_id), scheme_of_work_id, request.user.id)
    lesson = get_lesson_view.model

    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)
    
    key_stage_id = SchemeOfWorkModel.get_key_stage_id_only(db, int(scheme_of_work_id))

    model.lesson_id = lesson.id
    model.key_stage_id = key_stage_id

    solo_taxonomy_options = SoloTaxonomyModel.get_options(db)

    content_options = ContentModel.get_options(db, key_stage_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": 0,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    #231: pass the active model to ViewModel
    view_model = ViewModel("", lesson.title, "Edit: {}".format(model.description), data=data, active_model=model, alert_message=request.session.get("alert_message"))
    
    return render(request, "learningobjectives/edit.html", view_model.content)


@permission_required('cssow.publish_learningobjectivemodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ save_item non-view action """
    
    # create instance of model from request.vars

    model = LearningObjectiveModel(
        id_=request.POST.get("id", 0),
        description=request.POST.get("description", ""),
        solo_taxonomy_id=request.POST.get("solo_taxonomy_id", 0),
        content_id=request.POST.get("content_id", 0),
        key_stage_id=request.POST.get("key_stage_id", 0),
        lesson_id=lesson_id,
        key_words = request.POST.get("key_words", []),
        notes = request.POST.get("notes", ""),
        group_name = request.POST.get("group_name", ""),
        created=datetime.now(),
        created_by_id=request.user.id
    )

    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    viewmodel = LearningObjectiveSaveViewModel(db, model, request.user.id)
    
    model = viewmodel.model

    model.validate()
    
    if model.is_valid == True:
        
        ' save learning objectives'
        viewmodel.execute(int(request.POST["published"]))
        model = viewmodel.model
        
        ' save keywords '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('learningobjective.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """
        
        request.session["alert_message"] = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        redirect_to_url = reverse('learningobjective.edit', args=(scheme_of_work_id,lesson_id,learning_objective_id))

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_learningobjectivemodel', login_url='/accounts/login/')
def delete_unpublished(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    LearningObjectiveDeleteUnpublishedViewModel(db, lesson_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.publish_learningobjectivemodel', login_url='/accounts/login/')
def publish_item(request, scheme_of_work_id, lesson_id, learning_objective_id):
    ''' Publish the learningobjective '''
    #231: published item     
    redirect_to_url = request.META.get('HTTP_REFERER')

    LearningObjectivePulishModelViewModel(db, learning_objective_id, request.user.id)

    # TODO: redirect
    return HttpResponseRedirect(redirect_to_url)