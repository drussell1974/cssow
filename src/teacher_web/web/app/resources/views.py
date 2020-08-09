from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel

# TODO: use view models
from shared.models.cls_resource import ResourceModel
from shared.models.cls_lesson import LessonModel

# view models
from ..lessons.viewmodels import LessonGetModelViewModel
from ..resources.viewmodels import ResourceGetModelViewModel, ResourceGetAllViewModel, ResourceSaveViewModel

from shared.models.core import validation_helper

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from shared.filehandler import handle_uploaded_markdown


def index(request, scheme_of_work_id, lesson_id):
    ''' Get learning objectives for lesson '''
    getall_resources_view = ResourceGetAllViewModel(db, scheme_of_work_id, lesson_id, request.user.id)
    resources = getall_resources_view.model

    get_lesson_view = LessonGetModelViewModel(db, lesson_id, scheme_of_work_id, request.user.id)
    lesson = get_lesson_view.model

    lesson_options = LessonModel.get_options(db, scheme_of_work_id, request.user.id)  
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "lesson_id":int(lesson_id),
        "lesson": lesson,
        "resources": resources,
        "lesson_options": lesson_options
    }

    view_model = ViewModel(lesson.title, lesson.title, lesson.summary, data=data, active_model=lesson)
    
    return render(request, "resources/index.html", view_model.content)


def new(request, scheme_of_work_id, lesson_id):
    ''' Create a new resource '''

    model = ResourceModel(
        id_=0,
        title="",
        publisher="",
        scheme_of_work_id=scheme_of_work_id,
        lesson_id=lesson_id)

    get_lesson_view = LessonGetModelViewModel(db, int(lesson_id), scheme_of_work_id, request.user.id)
    lesson = get_lesson_view.model

    get_resource_type_options = ResourceModel.get_resource_type_options(db, request.user.id)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    view_model = ViewModel(lesson.title, lesson.title, "New", data=data)
    
    return render(request, "resources/edit.html", view_model.content)


def edit(request, scheme_of_work_id, lesson_id, resource_id):
    ''' Edit an existing resource '''
    
    get_model_view = ResourceGetModelViewModel(db, resource_id, lesson_id, scheme_of_work_id, request.user.id)
    model = get_model_view.model

    if model == None:
        model = ResourceModel(
            id_=0,
            title="",
            publisher="",
            scheme_of_work_id=scheme_of_work_id,
            lesson_id=lesson_id)


    get_lesson_view = LessonGetModelViewModel(db, int(lesson_id), scheme_of_work_id, request.user.id)    
    lesson = get_lesson_view.model

    get_resource_type_options = ResourceModel.get_resource_type_options(db, request.user.id)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    #231: pass the active model to ViewModel
    view_model = ViewModel(lesson.title, lesson.title, "Edit: {}".format(model.title), data=data, active_model=model, alert_message=request.session.get("alert_message"))
    
    return render(request, "resources/edit.html", view_model.content)


def save(request, scheme_of_work_id, lesson_id, resource_id):
    
    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        # set markdown document name with file name after saving
        model.md_document_name = f
        
    """ save_item non-view action """
    # create instance of model from request.vars
    model = ResourceModel(
        id_=resource_id,
        lesson_id=lesson_id,
        scheme_of_work_id=scheme_of_work_id,
        title=request.POST.get("title", ""),
        publisher=request.POST.get("publisher", ""),
        md_document_name=request.POST.get("md_document_name", ""),
        page_note=request.POST.get("page_note", ""),
        page_uri=request.POST.get("page_uri", ""),
        type_id=request.POST.get("type_id", None),  
        created=datetime.now(),
        created_by_id=request.user.id,
        published=request.POST.get("published", 0)
    )

    ResourceModel.MARKDOWN_TYPE_ID = settings.MARKDOWN_TYPE_ID

    ' set property if Markdown document is being uploaded '
    if model.type_id == settings.MARKDOWN_TYPE_ID and "md_file" in request.FILES:
        model.md_document_name = request.FILES['md_file']
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    save_resource_view = ResourceSaveViewModel(db, model, request.user.id)
    
    save_resource_view.execute(int(request.POST["published"]))

    model = save_resource_view.model
 

    if model.is_valid == True:
        ' save resource'

        ' upload file if Markdown document '
        if model.type_id == settings.MARKDOWN_TYPE_ID and "md_file" in request.FILES:
            handle_uploaded_markdown(request.FILES['md_file'], model, upload_success_handler, upload_error_handler)
            
        ' redirect as necessary '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
            
        else:
            redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """

        #request.session["alert_message"] = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        
        #redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id,lesson_id,resource_id))

        get_lesson_view = LessonGetModelViewModel(db, int(lesson_id), scheme_of_work_id, request.user.id)    
        lesson = get_lesson_view.model
            
        get_resource_type_options = ResourceModel.get_resource_type_options(db, request.user.id)

        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "lesson_id": lesson_id,
            "resource_id": model.id,
            "resource": model,
            "get_resource_type_options": get_resource_type_options,
            "validation_errors":model.validation_errors
        }
        view_model = ViewModel(lesson.title, lesson.summary, "Edit: {}".format(model.title), data=data, active_model=model, alert_message=request.session.get("alert_message"))
        
        return render(request, "resources/edit.html", view_model.content)

    return HttpResponseRedirect(redirect_to_url)


def delete_item(request, scheme_of_work_id, lesson_id, resource_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    ResourceModel.delete(db, resource_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)


def delete_unpublished(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    ResourceModel.delete_unpublished(db, lesson_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)


def publish_item(request, scheme_of_work_id, lesson_id, resource_id):
    ''' Publish the learningobjective '''
    #231: published item     
    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_resource.publish_item(db, resource_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)