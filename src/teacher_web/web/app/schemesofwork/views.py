from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.cls_schemeofwork import SchemeOfWorkModel 
from shared.models.cls_examboard import ExamBoardDataAccess
from shared.models.cls_keystage import KeyStageDataAccess
from shared.models.core import validation_helper
from datetime import datetime

from shared.view_model import ViewModel

from app.schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkSaveModelViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkGetAllViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkDeleteUnpublishedViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkPublishModelViewModel

# Create your views here.

def index(request):

    getall_view =  SchemeOfWorkGetAllViewModel(db, auth_user=request.user.id)
    
    data = {
        "schemes_of_work":getall_view.model
    }

    view_model = ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", data=data)

    return render(request, "schemesofwork/index.html", view_model.content)


@permission_required('cssow.add_schemeofworkmodel', login_url='/accounts/login/')
def new(request):
    """ Create new scheme of work """

    scheme_of_work = SchemeOfWorkModel(id_=0)

    examboard_options = ExamBoardDataAccess.get_options(db)
    keystage_options = KeyStageDataAccess.get_options(db)

    data = {
        "scheme_of_work_id": scheme_of_work.id,
        "scheme_of_work": scheme_of_work,
        "examboard_options": examboard_options,
        "keystage_options": keystage_options,
    }
 
    view_model = ViewModel("", "Schemes of Work", "New", data=data)

    return render(request, "schemesofwork/edit.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id):
    """ edit action """
    # TODO: Use ViewModel
    
    examboard_options = ExamBoardDataAccess.get_options(db)
    keystage_options = KeyStageDataAccess.get_options(db)


    if request.method == "GET":

        getmodel_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, request.user.id)
        model = getmodel_view.model
        
    elif request.method == "POST":
    
        # create instance of model from request.vars

        model = SchemeOfWorkModel(
            id_=request.POST.get("id", 0),
            name=request.POST.get("name", ""),
            description=request.POST.get("description", ""),
            exam_board_id=request.POST.get("exam_board_id", 0),
            key_stage_id=request.POST.get("key_stage_id", 0),
            created=datetime.now(),
            created_by_id=request.user.id)

        # validate the model and save if valid otherwise redirect to default invalid

        save_view = SchemeOfWorkSaveModelViewModel(db, model, request.user.id)
        save_view.execute(request.POST["published"])
        model = save_view.model

        if model.is_valid == True:
            ' save the lesson '

            if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
                redirect_to_url = request.POST.get("next", None)
            else:
                redirect_to_url = reverse('schemesofwork.edit', args=[model.id])
            return HttpResponseRedirect(redirect_to_url)


    data = {
        "scheme_of_work_id": model.id,
        "scheme_of_work": model,
        "examboard_options": examboard_options,
        "keystage_options": keystage_options,
    }

    view_model = ViewModel("", "Schemes of Work", model.name, data=data, active_model=model)

    return render(request, "schemesofwork/edit.html", view_model.content)


@permission_required('cssow.publish_schemeofworkmodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id):
    """ Save Scheme of Work """

    # create instance of model from request.vars

    model = SchemeOfWorkModel(
        id_=request.POST.get("id", 0),
        name=request.POST.get("name", ""),
        description=request.POST.get("description", ""),
        exam_board_id=request.POST.get("exam_board_id", 0),
        key_stage_id=request.POST.get("key_stage_id", 0),
        created=datetime.now(),
        created_by_id=request.user.id)

    # validate the model and save if valid otherwise redirect to default invalid

    save_view = SchemeOfWorkSaveModelViewModel(db, model, request.user.id)
    save_view.execute(request.POST["published"])
    model = save_view.model
    
    if model.is_valid == True:
        ' save the lesson '

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse('schemesofwork.edit', args=[model.id])
    else:
        """ redirect back to page and show message """
        request.session.alert_message = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        redirect_to_url = reverse('schemesofwork.edit', args=[scheme_of_work_id])

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
def delete_unpublished(request):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')
    # TODO: Use ViewModel

    SchemeOfWorkDeleteUnpublishedViewModel(db, auth_user=request.user.id)

    return HttpResponseRedirect(redirect_to_url)
