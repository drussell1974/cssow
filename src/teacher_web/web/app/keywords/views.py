from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from shared.models.enums.permissions import SCHEMEOFWORK
from shared.models.enums.publlished import STATE
from shared.models.decorators.permissions import min_permission_required
from shared.wizard_helper import WizardHelper
from shared.view_model import ViewModel
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel
from ..lessons.viewmodels import LessonGetModelViewModel
from ..schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from ..keywords.viewmodels import KeywordGetModelViewModel, KeywordGetAllListViewModel, KeywordSaveViewModel, KeywordDeleteUnpublishedViewModel, KeywordMergeViewModel
from shared.models.core import validation_helper
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@min_permission_required(SCHEMEOFWORK.VIEWER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def index(request, institute_id, department_id, scheme_of_work_id, auth_ctx):

    getall_keywords = KeywordGetAllListViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    
    return render(request, "keywords/index.html", getall_keywords.view(request).content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def new(request, institute_id, department_id, scheme_of_work_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    model = KeywordModel(
        id_=0,
        term="",
        definition="",
        scheme_of_work_id=scheme_of_work_id)

    # TODO: #386 wizard options
    wizard = WizardHelper(
        next_url=reverse('lesson.new', args=[institute_id, department_id, scheme_of_work_id]),
        add_another_url=reverse('keywords.new', args=[institute_id, department_id, scheme_of_work_id]),
        default_url=reverse('keywords.index', args=(institute_id, department_id, scheme_of_work_id))
    )

    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }
    
    view_model = ViewModel(request, scheme_of_work.name, scheme_of_work.name, "Scheme of work", content_heading="Keyword", ctx=auth_ctx, data=data, wizard=wizard)
    
    return render(request, "keywords/edit.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def edit(request, institute_id, department_id, scheme_of_work_id, keyword_id, auth_ctx):
    
    # TODO: #386 wizard options
    wizard = WizardHelper(
        next_url=reverse('lesson.new', args=[institute_id, department_id, scheme_of_work_id]),
        add_another_url=reverse('keywords.new', args=[institute_id, department_id, scheme_of_work_id]),
        default_url=reverse('keywords.index', args=(institute_id, department_id, scheme_of_work_id))
    )

    get_model_view = KeywordGetModelViewModel(db=db, keyword_id=keyword_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    model = get_model_view.model
    
    if model == None:
        model = KeywordModel(
            id_=0,
            term="",
            definition="",
            scheme_of_work_id=scheme_of_work_id)

    get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
    scheme_of_work = get_scheme_of_work_view.model

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "keyword_id": model.id,
        "keyword": model
    }

    view_model = ViewModel(request, scheme_of_work.name, scheme_of_work.name, "Edit keyword: {} for {}".format(model.term, scheme_of_work.description), ctx=auth_ctx, data=data, active_model=model, alert_message="", wizard=wizard)

    return render(request, "keywords/edit.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.EDITOR, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def save(request, institute_id, department_id, scheme_of_work_id, keyword_id, auth_ctx):

    def upload_error_handler(e, msg):
        print(msg, e)
    
    def upload_success_handler(f, msg):
        print(msg, f)
        
    #367 get auth_ctx from min_permission_required decorator
    
    error_message = ""

    """ save_item non-view action """
    published_state = STATE.parse(request.POST.get("published", "DRAFT"))
    model = KeywordModel(
        id_=keyword_id,
        scheme_of_work_id=scheme_of_work_id,
        term=request.POST.get("term", ""),
        definition=request.POST.get("definition", ""),
        created=datetime.now(),
        created_by_id=auth_ctx,
        published=published_state
    )
    
    # 299 Referenece KeywordModel - remove MARKDOWN_TYPE_ID
    
    # validate the model and save if valid otherwise redirect to default invalid
    redirect_to_url = ""

    save_keyword_view = KeywordSaveViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=0, model=model, auth_user=auth_ctx)
    
    save_keyword_view.execute(published_state)

    model = save_keyword_view.model
    
    # TODO: #386 wizard options
    wizard = WizardHelper(
        next_url=reverse('lesson.new', args=[institute_id, department_id, scheme_of_work_id]),
        add_another_url=reverse('keywords.new', args=[institute_id, department_id, scheme_of_work_id]),
        default_url=reverse('keywords.index', args=(institute_id, department_id, scheme_of_work_id))
    )

    if model.is_valid == True:
        ' save keyword '
  
        ' redirect as necessary '
        # TODO: #386 determine wizard mode
        redirect_to_url = wizard.get_redirect_url(request)
    else:
        """ redirect back to page and show message """

        get_scheme_of_work_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        scheme_of_work = get_scheme_of_work_view.model

        data = {
            "scheme_of_work_id": scheme_of_work_id,
            "keyword_id": model.id,
            "keyword": model
        }
        
        view_model = ViewModel(request, scheme_of_work.name, scheme_of_work.name, "Create new keyword for %s" % scheme_of_work.name, ctx=auth_ctx, data=data, active_model=model, alert_message="", error_message=error_message, wizard=wizard)        
        
        return render(request, "keywords/edit.html", view_model.content)
        
    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_item(request, institute_id, department_id, scheme_of_work_id, keyword_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    KeywordModel.delete(db, keyword_id, lesson_id=0, auth_user=auth_ctx)

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def publish_item(request, institute_id, department_id, scheme_of_work_id, lesson_id, keyword_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
        
    KeywordModel.publish_by_id(db, keyword_id, auth_ctx)

    return HttpResponseRedirect(reverse("keywords.index", args=[institute_id, department_id, scheme_of_work_id, lesson_id]))


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def delete_unpublished(request, institute_id, department_id, scheme_of_work_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    KeywordDeleteUnpublishedViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    return HttpResponseRedirect(reverse("schemesofwork.index", args=[institute_id, department_id]))


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(SCHEMEOFWORK.OWNER, login_url="/accounts/login/", login_route_name="team-permissions.login-as")
def merge_duplicates(request, institute_id, department_id, scheme_of_work_id, keyword_id, auth_ctx):

    #367 get auth_ctx from min_permission_required decorator
    
    merge_viewmodel = KeywordMergeViewModel(db=db, keyword_id=keyword_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)

    merge_viewmodel.execute(request)

    if merge_viewmodel.completed == True:
        ' redirect as necessary '
        return HttpResponseRedirect(merge_viewmodel.redirect_to_url)
    
    return render(request, "keywords/merge.html", merge_viewmodel.view(request).content)
    