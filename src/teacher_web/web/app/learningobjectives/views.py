from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel

from .viewmodels import LearningObjectiveEditViewModel
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

from shared.models.core.basemodel import try_int
from shared.models.core import validation_helper
from shared.models.core.django_helper import auth_user_id
from shared.models.core.log import handle_log_warning

# view models
from app.lessons.viewmodels import LessonGetModelViewModel


def index(request, scheme_of_work_id, lesson_id):
    ''' Get learning objectives for lesson '''

    #253 check user id
    learningobjectivesviewmodel = LearningObjectiveIndexViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
    
    return render(request, "learningobjectives/index.html", learningobjectivesviewmodel.view().content)


@permission_required('cssow.add_learningobjectivemodel', login_url='/accounts/login/')
def new(request, scheme_of_work_id, lesson_id):
    ''' Create a new learning objective '''

    # check if an existing_learning_objective_id has been passed
     
    #253 check user id 
    get_lessonobjective_view = LearningObjectiveGetModelViewModel(db=db, learning_objective_id=0, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_user_id(request))
    model = get_lessonobjective_view.model
    
    #253 check user id
    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
    lesson = get_lesson_view.model

    if scheme_of_work_id is not None:
        # required for creating a new object
        get_lessonobjective_view.model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        get_lessonobjective_view.model.lesson_id = int(lesson_id)

    #270 set default content from lesson and solo taxonomy
 
    if model.content_id is None or model.content_id == 0:
        model.content_id = lesson.content_id
    
    if model.solo_taxonomy_id is None or model.solo_taxonomy_id == 0:
        model.solo_taxonomy_id = int(request.GET.get("solo", "0"))
 
    key_stage_id = SchemeOfWorkModel.get_key_stage_id_only(db, int(scheme_of_work_id), auth_user_id(request))

    get_lessonobjective_view.model.lesson_id = lesson.id
    get_lessonobjective_view.model.key_stage_id = key_stage_id

    solo_taxonomy_options = SoloTaxonomyModel.get_options(db, auth_user_id(request))

    content_options = ContentModel.get_options(db, key_stage_id, auth_user_id(request))
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": 0,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    
    view_model = ViewModel("", lesson.title, "Create new learning objective for %s" % lesson.title, data=data)
    
    return render(request, "learningobjectives/edit.html", view_model.content)


@permission_required('cssow.change_learningobjectivemodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, lesson_id, learning_objective_id = 0):
    ''' Edit an existing learning objective '''
    
    if request.method == "GET":
        ## GET request from client ##
    
        #253 check user id
        get_model_viewmodel = LearningObjectiveGetModelViewModel(db=db, learning_objective_id=learning_objective_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
        model = get_model_viewmodel.model


    elif request.method == "POST":
        ## POST back from client ##
        # create instance of model from request

        model = LearningObjectiveModel(
            id_=request.POST.get("id", 0),
            description=request.POST.get("description", ""),
            solo_taxonomy_id=try_int(request.POST.get("solo_taxonomy_id", 0)),
            content_id=request.POST.get("content_id", 0),
            key_stage_id=request.POST.get("key_stage_id", 0),
            lesson_id=lesson_id,
            key_words = request.POST.get("key_words", []),
            notes = request.POST.get("notes", ""),
            group_name = request.POST.get("group_name", ""),
            created=datetime.now(),
            #253 check user id
            created_by_id=auth_user_id(request)
        )

        # validate the model and save if valid otherwise redirect to default invalid
        redirect_to_url = ""

        #253 check user id
        viewmodel = LearningObjectiveEditViewModel(db=db, scheme_of_work_id=scheme_of_work_id, model=model, auth_user=auth_user_id(request))
        
        viewmodel.execute(int(request.POST["published"]))
        model = viewmodel.model
            
        if model.is_valid == True:
            
            redirect_to_url = reverse('learningobjective.index', args=(scheme_of_work_id, model.id))
            
            if request.POST["next"] != None and request.POST["next"] != "":
                redirect_to_url = request.POST["next"]

            return HttpResponseRedirect(redirect_to_url)
        else:
            handle_log_warning(db, "learning objective {} (id:{}) is invalid posting back to client - {}".format(model.description, model.id, model.validation_errors))
            

    #253 check user id
    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
    lesson = get_lesson_view.model

    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
            
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)
        
    #270 set default content from lesson and solo taxonomy

    if model.content_id is None or model.content_id == 0:
        model.content_id = lesson.content_id
    
    if model.solo_taxonomy_id is None or model.solo_taxonomy_id == 0:
        model.solo_taxonomy_id = try_int(request.GET.get("solo", 0))

    if model.lesson_id is None or model.lesson_id == 0:  
        model.lesson_id = lesson.id
    
    key_stage_id = SchemeOfWorkModel.get_key_stage_id_only(db, int(scheme_of_work_id), auth_user_id(request))

    model.key_stage_id = key_stage_id

    solo_taxonomy_options = SoloTaxonomyModel.get_options(db, auth_user_id(request))

    content_options = ContentModel.get_options(db, key_stage_id, auth_user_id(request))
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": model.id,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    #231: pass the active model to ViewModel
    view_model = ViewModel("", lesson.title, "Edit: {}".format(model.description) if model.id > 0 else "Create new learning objective for %s" % lesson.title, data=data, active_model=model, alert_message="")
    
    return render(request, "learningobjectives/edit.html", view_model.content)


@permission_required('cssow.publish_learningobjectivemodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ save_item non-view action """

    # create instance of model from request

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
        #253 check user id
        created_by_id=auth_user_id(request)
    )

    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    #253 check user id
    viewmodel = LearningObjectiveEditViewModel(db=db, scheme_of_work_id=scheme_of_work_id, model=model, auth_user=auth_user_id(request))
    
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

    #253 check user id
    LearningObjectiveDeleteUnpublishedViewModel(db=db, lesson_id=lesson_id, auth_user=auth_user_id(request))

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.publish_learningobjectivemodel', login_url='/accounts/login/')
def publish_item(request, scheme_of_work_id, lesson_id, learning_objective_id):
    ''' Publish the learningobjective '''
    #231: published item     
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    LearningObjectivePulishModelViewModel(db=db, learning_objective_id=learning_objective_id, auth_user=auth_user_id(request))

    # redirect
    return HttpResponseRedirect(redirect_to_url)