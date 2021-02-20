from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.filehandler import handle_uploaded_markdown
from shared.models.core.context import AuthCtx
from shared.models.core import validation_helper
from shared.models.enums.permissions import LESSON
from shared.models.cls_resource import ResourceModel
from shared.models.cls_lesson import LessonModel
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from ..lessons.viewmodels import LessonGetModelViewModel
from ..resources.viewmodels import ResourceGetModelViewModel, ResourceIndexViewModel, ResourceSaveViewModel

@min_permission_required(LESSON.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, lesson_id):
    
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    getall_resources = ResourceIndexViewModel(db=db, request=request, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)  
    
    return render(request, "resources/index.html", getall_resources.view().content)


#234 add permission
@permission_required('cssow.add_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def new(request, institute_id, department_id, scheme_of_work_id, lesson_id):
    ''' Create a new resource '''
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    model = ResourceModel(
        id_=0,
        title="",
        publisher="",
        scheme_of_work_id=scheme_of_work_id,
        lesson_id=lesson_id)

    #253 check user id
    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    lesson = get_lesson_view.model

    #253 check user id
    get_resource_type_options = ResourceModel.get_resource_type_options(db, auth_user=auth_ctx)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    view_model = ViewModel(lesson.title, lesson.title, "Create new resource for %s" % lesson.title, ctx=auth_ctx, data=data)
    
    return render(request, "resources/edit.html", view_model.content)


#234 add permission
@permission_required('cssow.change_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, lesson_id, resource_id):
    ''' Edit an existing resource '''
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    #253 check user id
    get_model_view = ResourceGetModelViewModel(db=db, resource_id=resource_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_model_view.model

    if model == None:
        model = ResourceModel(
            id_=0,
            title="",
            publisher="",
            scheme_of_work_id=scheme_of_work_id,
            lesson_id=lesson_id)


    #253 check user id
    get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=int(lesson_id), scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)    
    lesson = get_lesson_view.model

    #253 check user id
    get_resource_type_options = ResourceModel.get_resource_type_options(db, auth_ctx)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson_id,
        "resource_id": model.id,
        "resource": model,
        "get_resource_type_options": get_resource_type_options,
    }
    
    #231: pass the active model to ViewModel
    view_model = ViewModel(lesson.title, lesson.title, "Edit: {}".format(model.title), ctx=auth_ctx, data=data, active_model=model, alert_message="")
    
    return render(request, "resources/edit.html", view_model.content)


#234 add permission
@permission_required('cssow.publish_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def save(request, institute_id, department_id, scheme_of_work_id, lesson_id, resource_id):
    
    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        # set markdown document name with file name after saving
        model.md_document_name = f
        
    error_message = ""

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
        #253 check user id
        created_by_id=auth_ctx.auth_user_id,
        published=request.POST.get("published", 0)
    )

    ResourceModel.MARKDOWN_TYPE_ID = settings.MARKDOWN_TYPE_ID

    ' set property if Markdown document is being uploaded '
    if model.type_id == settings.MARKDOWN_TYPE_ID and "md_file" in request.FILES:
        model.md_document_name = request.FILES['md_file']
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    #253 check user id
    save_resource_view = ResourceSaveViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, model=model, auth_user=auth_ctx)
    
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

        #redirect_to_url = reverse('resource.edit', args=(scheme_of_work_id,lesson_ischemesofwork.index scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)    
        lesson = get_lesson_view.model
            
        #253 check user id
        get_resource_type_options = ResourceModel.get_resource_type_options(db, auth_user=auth_ctx)

        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "lesson_id": lesson_id,
            "resource_id": model.id,
            "resource": model,
            "get_resource_type_options": get_resource_type_options,
            "validation_errors":model.validation_errors
        }
        view_model = ViewModel(lesson.title, lesson.summary, "Edit: {}".format(model.title), ctx=auth_ctx, data=data, active_model=model, alert_message="", error_message=error_message)
        
        return render(request, "resources/edit.html", view_model.content)

    return HttpResponseRedirect(redirect_to_url)


#234 add permission
@permission_required('cssow.delete_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, resource_id):
    """ delete item and redirect back to referer """

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    ResourceModel.delete(db, resource_id, auth_user=auth_ctx)

    return HttpResponseRedirect(redirect_to_url)


#234 add permission
@permission_required('cssow.delete_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    ResourceModel.delete_unpublished(db, lesson_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("resource.index", args=[institute_id, department_id, scheme_of_work_id, lesson_id]))


#234 add permission
@permission_required('cssow.publish_resource', login_url='/accounts/login/')
@min_permission_required(LESSON.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, resource_id):
    ''' Publish the learningobjective '''

    auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    ResourceModel.publish_item(db=db, scheme_of_work_id=scheme_of_work_id, resource_id=resource_id, auth_user=auth_ctx)
    
    return HttpResponseRedirect(reverse("resource.index", args=[institute_id, department_id, scheme_of_work_id, lesson_id]))
