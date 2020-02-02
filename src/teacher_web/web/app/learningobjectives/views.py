from datetime import datetime

from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from cssow.models import cls_lesson, cls_learningobjective, cls_schemeofwork, cls_solotaxonomy, cls_content, cls_examboard
from cssow.models.core import validation_helper


def index(request, scheme_of_work_id, lesson_id):
    ''' Get learning objectives for lesson '''

    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)
    learning_objectives = cls_learningobjective.get_all(db, lesson_id, request.user.id)
    
    lesson_options = cls_lesson.get_options(db, scheme_of_work_id, request.user.id)  
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "lesson_id":int(lesson_id),
        "lesson": lesson,
        "learning_objectives": learning_objectives,
        "lesson_options": lesson_options,
    }

    view_model = ViewModel("", lesson["title"], lesson["summary"], data=data)
    
    return render(request, "learningobjectives/index.html", view_model.content)


def new(request, scheme_of_work_id, lesson_id):
    ''' Create a new learning objective '''
    print('Creating a new learning objective...')

    # check if an existing_learning_objective_id has been passed
     
    model = cls_learningobjective.get_new_model(db, 0, request.user.id)

    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)
        
    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)

    key_stage_id = cls_schemeofwork.get_key_stage_id_only(db, int(scheme_of_work_id))

    model.lesson_id = lesson["id"]
    model.key_stage_id = key_stage_id

    solo_taxonomy_options = cls_solotaxonomy.get_options(db)

    content_options = cls_content.get_options(db, key_stage_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": 0,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    
    view_model = ViewModel("", lesson["title"], "New", data=data)
    
    return render(request, "learningobjectives/edit.html", view_model.content)


def edit(request, scheme_of_work_id, lesson_id, learning_objective_id):
    ''' Edit an existing learning objective '''
    
    cls_learningobjective.enable_logging = True
    model = cls_learningobjective.get_model(db, learning_objective_id, request.user.id)
    
    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)

    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)
    
    key_stage_id = cls_schemeofwork.get_key_stage_id_only(db, int(scheme_of_work_id))

    model.lesson_id = lesson["id"]
    model.key_stage_id = key_stage_id

    solo_taxonomy_options = cls_solotaxonomy.get_options(db)

    content_options = cls_content.get_options(db, key_stage_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "learning_objective_id": 0,
        "learningobjective": model,
        "solo_taxonomy_options": solo_taxonomy_options,
        "content_options": content_options,
    }
    
    view_model = ViewModel("", lesson["title"], "Edit: {}".format(model.description), data=data, alert_message=request.session.get("alert_message", None))
    
    return render(request, "learningobjectives/edit.html", view_model.content)


def save(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ save_item non-view action """
    print('saving learning objective... scheme_of_work_id:', scheme_of_work_id, ", lesson_id:", lesson_id, ", learning_objective_id:", learning_objective_id)
    
    # create instance of model from request.vars

    model = cls_learningobjective.LearningObjectiveModel(
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

    model.validate()
    
    print("saving learning objective - model.is_valid:", model.is_valid, ", model.validation_errors:", model.validation_errors)
    
    if model.is_valid == True:
        
        ' save learning objectives'
        cls_learningobjective.enable_logging = True
        model = cls_learningobjective.save(db, model, int(request.POST["published"]))

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


def delete_item(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_learningobjective.delete(db, request.user.id, learning_objective_id)

    return HttpResponseRedirect(redirect_to_url)

    
def delete_unpublished(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_learningobjective.delete_unpublished(db, lesson_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)