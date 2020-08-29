from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.cls_schemeofwork import SchemeOfWorkModel 
from shared.models.cls_examboard import ExamBoardModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.core.django_helper import auth_user_id
from shared.models.core.log import handle_log_warning, handle_log_info
from shared.models.core import validation_helper
from datetime import datetime

from shared.view_model import ViewModel

from app.schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkIndexViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkDeleteUnpublishedViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkPublishModelViewModel

# Create your views here.

def index(request):

    #253 check user id
    getall_view =  SchemeOfWorkIndexViewModel(db, auth_user=auth_user_id(request))
    
    data = {
        "schemes_of_work":getall_view.model
    }

    view_model = ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", data=data)

    return render(request, "schemesofwork/index.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id = 0):
    """ edit action """
    # TODO: Use ViewModel
    # initiate empty model 
    error_message = ""

    model = SchemeOfWorkModel(id_=scheme_of_work_id)
    
    if request.method == "GET" and model.id > 0:
        ## GET request from client ##

        #253 check user id
        getmodel_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, auth_user_id(request))
        model = getmodel_view.model
        
    elif request.method == "POST":
        ## POST back from client ##
        
        # create instance of model from request.vars

        model = SchemeOfWorkModel(
            id_=request.POST.get("id", 0),
            name=request.POST.get("name", ""),
            description=request.POST.get("description", ""),
            exam_board_id=request.POST.get("exam_board_id", 0),
            key_stage_id=request.POST.get("key_stage_id", 0),
            created=datetime.now(),
            #253 check user id
            created_by_id=auth_user_id(request))
    
        # validate the model and save if valid otherwise redirect to default invalid
        try:
            #253 check user id
            save_view = SchemeOfWorkEditViewModel(db, model, auth_user_id(request))
            save_view.execute(request.POST["published"])
            model = save_view.model

            if model.is_valid == True:
                ' save the lesson '

                if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
                    redirect_to_url = request.POST.get("next", None)
                else:
                    redirect_to_url = reverse('schemesofwork.edit', args=[model.id])
                return HttpResponseRedirect(redirect_to_url)
            else:
                handle_log_warning(db, "scheme of work {} (id:{}) is invalid posting back to client - {}".format(model.name, model.id, model.validation_errors))
        
        except Exception as e:
            error_message = e

    # get options
    examboard_options = ExamBoardModel.get_options(db, auth_user_id(request))
    keystage_options = KeyStageModel.get_options(db, auth_user_id(request))

    # view data
    data = {
        "scheme_of_work_id": model.id,
        "scheme_of_work": model,
        "examboard_options": examboard_options,
        "keystage_options": keystage_options,
    }
    
    # build alert message to be displayed
    delete_message = "<p>'{display_name}' ({id}) will be deleted!<ul>".format(display_name=model.name, id=model.id)
    if model.number_of_lessons > 0:
        delete_message = delete_message + "<li>{number_of_lessons} lesson(s)</li>".format(number_of_lessons=model.number_of_lessons)
    if model.number_of_learning_objectives > 0:
        delete_message = delete_message + "<li>{number_of_learning_objectives} learning objective(s)</li>".format(number_of_learning_objectives=model.number_of_learning_objectives)
    if model.number_of_resources > 0:
        delete_message = delete_message + "<li>{number_of_resources} resource(s)</li>".format(number_of_resources=model.number_of_resources)
    delete_message = delete_message + "</ul>"

    view_model = ViewModel("", "Schemes of Work", model.name if len(model.name) != 0 else "Create new scheme of work", data=data, active_model=model, error_message=error_message, alert_message="", delete_dialog_message=delete_message)

    return render(request, "schemesofwork/edit.html", view_model.content)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
def delete_unpublished(request):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')
    # TODO: Use ViewModel

    #253 check user id
    SchemeOfWorkDeleteUnpublishedViewModel(db, auth_user=auth_user_id(request))

    return HttpResponseRedirect(redirect_to_url)
