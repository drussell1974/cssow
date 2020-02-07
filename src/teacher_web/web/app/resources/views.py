from datetime import datetime

from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from cssow.models import cls_resource, cls_lesson, cls_schemeofwork
from cssow.models.core import validation_helper


def index(request, scheme_of_work_id, lesson_id):
    ''' Get learning objectives for lesson '''
    cls_resource.enable_logging = True
    resources = cls_resource.get(db, scheme_of_work_id, lesson_id, request.user.id)

    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)
    
    lesson_options = cls_lesson.get_options(db, scheme_of_work_id, request.user.id)  #TODO: create view_learningepisiode_options: remove this line

    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "lesson_id":int(lesson_id),
        "lesson": lesson,
        "resources": resources,
        "lesson_options": lesson_options
    }

    view_model = ViewModel("", lesson["title"], lesson["summary"], data=data)
    
    return render(request, "resources/index.html", view_model.content)


def new(request, scheme_of_work_id, lesson_id):
    ''' Create a new learning objective '''
    print('Creating a new learning objective...')

    # check if an existing_learning_objective_id has been passed
     
    model = cls_resource.get_new_model(db, 0, request.user.id)

    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)
        
    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource": model,
    }
    
    view_model = ViewModel("", lesson["title"], "New", data=data)
    
    return render(request, "resources/edit.html", view_model.content)


def edit(request, scheme_of_work_id, lesson_id, resource_id):
    ''' Edit an existing learning objective '''
    
    cls_resource.enable_logging = True
    model = cls_resource.get_model(db, resource_id, scheme_of_work_id, request.user.id)
    
    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)

    if scheme_of_work_id is not None:
        # required for creating a new object
        model.scheme_of_work_id = int(scheme_of_work_id)
        
    if lesson_id is not None:
        # required for creating a new object
        model.lesson_id = int(lesson_id)
    
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
    }
    
    view_model = ViewModel("", lesson["title"], "Edit: {}".format(model.title), data=data, alert_message=request.session.get("alert_message", None))
    
    return render(request, "resources/edit.html", view_model.content)


def save(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ save_item non-view action """
    print('saving resource... scheme_of_work_id:', scheme_of_work_id, ", lesson_id:", lesson_id)
    
    # create instance of model from request.vars

    model = cls_resource.Resource(
        id_=request.POST.get("id", 0),
        created=datetime.now(),
        created_by_id=request.user.id
    )

    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    model.validate()
    
    print("saving resource - model.is_valid:", model.is_valid, ", model.validation_errors:", model.validation_errors)
    
    if model.is_valid == True:
        
        ' save learning objectives'
        #cls_resource.enable_logging = True
        model = cls_resource.save(db, model, int(request.POST["published"]))

        ' save keywords '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """
        
        request.session["alert_message"] = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id,lesson_id,learning_objective_id))

    return HttpResponseRedirect(redirect_to_url)


def delete_item(request, scheme_of_work_id, lesson_id, learning_objective_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_resource.delete(db, request.user.id, learning_objective_id)

    return HttpResponseRedirect(redirect_to_url)


def delete_unpublished(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_resource.delete_unpublished(db, lesson_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)