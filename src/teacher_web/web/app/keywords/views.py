from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.core.context import Ctx
from shared.models.core.django_helper import auth_user_model
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from ..lessons.viewmodels import LessonGetModelViewModel
from ..schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from ..keywords.viewmodels import KeywordGetModelViewModel, KeywordGetAllListViewModel, KeywordSaveViewModel, KeywordDeleteUnpublishedViewModel, KeywordMergeViewModel
from shared.models.core import validation_helper
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from shared.filehandler import handle_uploaded_markdown


@min_permission_required(SCHEMEOFWORK.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id):
    ''' Get keywords for scheme of work '''

    view_ctx = Ctx(institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)

    #253 check user id
    getall_keywords = KeywordGetAllListViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    return render(request, "keywords/index.html", getall_keywords.view().content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def new(request, institute_id, department_id, scheme_of_work_id):
    ''' Create a new keyword '''

    model = KeywordModel(
        id_=0,
        term="",
        definition="",
        scheme_of_work_id=scheme_of_work_id)
    
    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }
    
    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Create new keyword for %s" % scheme_of_work.name, ctx=None, data=data)
    
    return render(request, "keywords/edit.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, keyword_id):
    ''' Edit an existing keyword '''

    get_model_view = KeywordGetModelViewModel(db=db, keyword_id=keyword_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))
    model = get_model_view.model
    
    if model == None:
        model = KeywordModel(
            id_=0,
            term="",
            definition="",
            scheme_of_work_id=scheme_of_work_id)

    #253 check user id

    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }

    view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Edit keyword: {} for {}".format(model.term, scheme_of_work.description), ctx=None, data=data, active_model=model, alert_message="")
    
    return render(request, "keywords/edit.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def save(request, institute_id, department_id, scheme_of_work_id, keyword_id):
    
    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        
    error_message = ""

    """ save_item non-view action """
    model = KeywordModel(
        id_=keyword_id,
        scheme_of_work_id=scheme_of_work_id,
        term=request.POST.get("term", ""),
        definition=request.POST.get("definition", ""),
        created=datetime.now(),
        #253 check user id
        created_by_id=auth_user_model(db, request),
        published=request.POST.get("published", 0)
    )
    
    # 299 Referenece KeywordModel - remove MARKDOWN_TYPE_ID
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    #253 check user id
    save_keyword_view = KeywordSaveViewModel(db=db, scheme_of_work_id=scheme_of_work_id, model=model, auth_user=auth_user_model(db, request))
    
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

        get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))
        scheme_of_work = get_scheme_of_work_view.model

        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "keyword_id": model.id,
            "keyword": model,
            "validation_errors":model.validation_errors
        }
        
        view_model = ViewModel(scheme_of_work.name, scheme_of_work.name, "Create new keyword for %s" % scheme_of_work.name, ctx=None, data=data, active_model=model, alert_message="", error_message=error_message)        
        
        return render(request, "keywords/edit.html", view_model.content)
        
    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_item(request, institute_id, department_id, scheme_of_work_id, keyword_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    #253 check user id
    KeywordModel.delete(db, keyword_id, auth_user_model(db, request))

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id):
    ''' Publish the keyword '''

    KeywordModel.publish_by_id(db, keyword_id, auth_user_model(db, request))

    return HttpResponseRedirect(reverse("keywords.index", args=[scheme_of_work_id, lesson_id]))


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id):
    """ delete item and redirect back to referer """

    view_ctx = Ctx(institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

    # TODO: #329 move to view model
    auth_ctx = auth_user_model(db, request, ctx=view_ctx)

    KeywordDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("schemesofwork.index", args=[institute_id, department_id]))


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def merge_duplicates(request, institute_id, department_id, scheme_of_work_id, keyword_id):
    """ delete item and redirect back to referer """

    merge_viewmodel = KeywordMergeViewModel(db=db, keyword_id=keyword_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_model(db, request))

    merge_viewmodel.execute(request)

    if merge_viewmodel.completed == True:
        ' redirect as necessary '
        return HttpResponseRedirect(merge_viewmodel.redirect_to_url)
    
    return render(request, "keywords/merge.html", merge_viewmodel.view().content)
    