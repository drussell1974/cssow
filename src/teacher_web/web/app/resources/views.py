from datetime import datetime
from django import forms
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from shared.models import cls_resource, cls_lesson, cls_schemeofwork
from shared.models.core import validation_helper

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from shared.filehandler import handle_uploaded_markdown


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
    ''' Create a new resource '''
    print('Creating a new resource...')

    model = cls_resource.ResourceModel(
        id_=0,
        title="",
        publisher="",
        scheme_of_work_id=scheme_of_work_id,
        lesson_id=lesson_id)

    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)
    get_resource_type_options = cls_resource.get_resource_type_options(db, request.user.id)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    view_model = ViewModel("", lesson["title"], "New", data=data)
    
    return render(request, "resources/edit.html", view_model.content)


def edit(request, scheme_of_work_id, lesson_id, resource_id):
    ''' Edit an existing resource '''
    
    cls_resource.enable_logging = True
    model = cls_resource.get_model(db, resource_id, scheme_of_work_id, request.user.id)

    if model == None:
        model = cls_resource.ResourceModel(
            id_=0,
            title="",
            publisher="",
            scheme_of_work_id=scheme_of_work_id,
            lesson_id=lesson_id)


    lesson = cls_lesson.get_model(db, int(lesson_id), request.user.id)    
    get_resource_type_options = cls_resource.get_resource_type_options(db, request.user.id)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    view_model = ViewModel("", lesson["title"], "Edit: {}".format(model.title), data=data, alert_message=request.session.get("alert_message", None))
    
    return render(request, "resources/edit.html", view_model.content)


def save(request, scheme_of_work_id, lesson_id, resource_id):
    
    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        # set markdown document name with file name after saving
        model.md_document_name = f
        
    """ save_item non-view action """
    print('saving resource... scheme_of_work_id:', scheme_of_work_id, ", lesson_id:", lesson_id)
    # create instance of model from request.vars
    cls_resource.enable_logging = True
    model = cls_resource.ResourceModel(
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

    ' upload file if Markdown document '
    if model.type_id == cls_resource.MARKDOWN_TYPE_ID and "md_file" in request.FILES:
        handle_uploaded_markdown(request.FILES['md_file'], model, upload_success_handler, upload_error_handler)
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    model.validate()

    print("saving resource - model.is_valid:", model.is_valid, ", model.validation_errors:", model.validation_errors)
    
    if model.is_valid == True:
        ' save resource'
        #cls_resource.enable_logging = True
        model = cls_resource.save(db, model, int(request.POST["published"]))

        ' redirect as necessary '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """

        request.session["alert_message"] = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        
        redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id,lesson_id,resource_id))

    return HttpResponseRedirect(redirect_to_url)


def delete_item(request, scheme_of_work_id, lesson_id, resource_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_resource.delete(db, resource_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)


def delete_unpublished(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_resource.delete_unpublished(db, lesson_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)