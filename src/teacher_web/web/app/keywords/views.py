from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from shared.models.core.django_helper import auth_user_id
from shared.view_model import ViewModel

# TODO: use view models
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel

# view models
from ..lessons.viewmodels import LessonGetModelViewModel
from ..schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from ..keywords.viewmodels import KeywordGetModelViewModel, KeywordGetAllListViewModel, KeywordSaveViewModel, KeywordDeleteUnpublishedViewModel

from shared.models.core import validation_helper

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from shared.filehandler import handle_uploaded_markdown

# 299 Keyword Index
def index(request, scheme_of_work_id):
    ''' Get keywords for scheme of work '''
    #253 check user id
    getall_keywords = KeywordGetAllListViewModel(db, request, scheme_of_work_id, auth_user_id(request))  
    
    # TODO: 299 create keywords/index.html page
    return render(request, "keywords/index.html", getall_keywords.view().content)


# TODO: 299 create new
# TODO: 299 add permission
@permission_required('cssow.add_resource', login_url='/accounts/login/')
def new(request, scheme_of_work_id):
    ''' Create a new keyword '''

    model = KeywordModel(
        id_=0,
        term="",
        definition="",
        scheme_of_work_id=scheme_of_work_id)
    
    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, auth_user_id(request))
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Create new keyword for %s" % scheme_of_work.name, data=data)
    
    return render(request, "keywords/edit.html", view_model.content)


# TODO: 299 edit exiting
# TODO: 299 add permission
@permission_required('cssow.change_resource', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, keyword_id):
    ''' Edit an existing keyword '''

    # TODO: 299 KeywordGetModelViewModel
    get_model_view = KeywordGetModelViewModel(db, keyword_id, scheme_of_work_id, auth_user_id(request))
    model = get_model_view.model
    
    if model == None:
        model = KeywordModel(
            id_=0,
            term="",
            definition="",
            scheme_of_work_id=scheme_of_work_id)

    #253 check user id

    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, auth_user_id(request))
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }

    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit keyword: {} for {}".format(model.term, scheme_of_work.description), data=data, active_model=model, alert_message="")
    
        # TODO: 299 create keywords/edit.html page
    return render(request, "keywords/edit.html", view_model.content)


# TODO: 299 save
# TODO: 299 add permission
@permission_required('cssow.publish_resource', login_url='/accounts/login/')
def save(request, scheme_of_work_id, keyword_id):
    
    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        
    error_message = ""

    """ save_item non-view action """
    # create instance of model from request.vars
    # TODO: 299 reference KeywordModel id, term, definition
    model = KeywordModel(
        id_=keyword_id,
        scheme_of_work_id=scheme_of_work_id,
        term=request.POST.get("term", ""),
        definition=request.POST.get("definition", ""),
        created=datetime.now(),
        #253 check user id
        created_by_id=auth_user_id(request),
        published=request.POST.get("published", 0)
    )
    
    # 299 Referenece KeywordModel - remove MARKDOWN_TYPE_ID
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    #253 check user id
    # TODO: 299 Reference KeywordSaveViewModel
    save_keyword_view = KeywordSaveViewModel(db, model, auth_user_id(request))
    
    save_keyword_view.execute(int(request.POST["published"]))

    model = save_keyword_view.model
    

    if model.is_valid == True:
        ' save keyword '
  
        ' redirect as necessary '
        if request.POST["next"] != None and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('keyword.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """

        get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, auth_user_id(request))
        scheme_of_work = get_scheme_of_work_view.model

        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "keyword_id": model.id,
            "keyword": model,
            "validation_errors":model.validation_errors
        }
        
        view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Create new keyword for %s" % scheme_of_work.name, data=data, active_model=model, alert_message="", error_message=error_message)        
        
        return render(request, "keywords/edit.html", view_model.content)
        
    return HttpResponseRedirect(redirect_to_url)


# TODO: 299 add permission
@permission_required('cssow.delete_resource', login_url='/accounts/login/')
def delete_item(request, scheme_of_work_id, lesson_id, keyword_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    # TODO: 299 delete by keyword_id
    ResourceModel.delete(db, keyword_id, auth_user_id(request))

    return HttpResponseRedirect(redirect_to_url)


# TODO: 299 add permission
@permission_required('cssow.publish_resource', login_url='/accounts/login/')
def publish_item(request, scheme_of_work_id, lesson_id, keyword_id):
    ''' Publish the keyword '''
    #231: published item     
    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    cls_keyword.publish_item(db, keyword_id, auth_user_id(request))

    return HttpResponseRedirect(redirect_to_url)


# TODO: 299 add permission
@permission_required('cssow.delete_resource', login_url='/accounts/login/')
def delete_unpublished(request, scheme_of_work_id, lesson_id = 0):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')
    # TODO: Use ViewModel

    #253 check user id
    KeywordDeleteUnpublishedViewModel(db, scheme_of_work_id, lesson_id, auth_user=auth_user_id(request))

    return HttpResponseRedirect(redirect_to_url)