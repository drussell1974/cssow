from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models import cls_schemeofwork, cls_examboard, cls_keystage
from shared.models.core import validation_helper
from datetime import datetime
from shared.view_model import ViewModel


# Create your views here.

def index(request):
    schemes_of_work = cls_schemeofwork.get_all(db, key_stage_id=0, auth_user=request.user.id)
    
    data = {
        "schemes_of_work":schemes_of_work
    }

    view_model = ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", data=data)

    return render(request, "schemesofwork/index.html", view_model.content)


@permission_required('cssow.add_schemeofworkmodel', login_url='/accounts/login/')
def new(request):
    """ Create new scheme of work """

    scheme_of_work = cls_schemeofwork.SchemeOfWorkModel(id_=0)

    examboard_options = cls_examboard.get_options(db)
    keystage_options = cls_keystage.get_options(db)

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

    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)

    examboard_options = cls_examboard.get_options(db)
    keystage_options = cls_keystage.get_options(db)

    data = {
        "scheme_of_work_id": scheme_of_work.id,
        "scheme_of_work": scheme_of_work,
        "examboard_options": examboard_options,
        "keystage_options": keystage_options,
    }
 
    view_model = ViewModel("", "Schemes of Work", scheme_of_work.name, data=data)

    return render(request, "schemesofwork/edit.html", view_model.content)
    

@permission_required('cssow.publish_schemeofworkmodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id):
    """ Save Scheme of Work """

    # create instance of model from request.vars

    model = cls_schemeofwork.SchemeOfWorkModel(
        id_=request.POST.get("id", 0),
        name=request.POST.get("name", ""),
        description=request.POST.get("description", ""),
        exam_board_id=request.POST.get("exam_board_id", 0),
        key_stage_id=request.POST.get("key_stage_id", 0),
        created=datetime.now(),
        created_by_id=request.user.id)

    # validate the model and save if valid otherwise redirect to default invalid

    published = request.POST["published"]
    
    model.validate()

    print("saving... model.is_valid :", model.is_valid)
        
    if model.is_valid == True:
        ' save the lesson '
        cls_schemeofwork.enable_logging = True
        model = cls_schemeofwork.save(db, model, published)
        
        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse('schemesofwork.edit', args=[model.id])
    else:
        """ redirect back to page and show message """
        request.session.alert_message = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        print("saving... scheme_of_work_id:", scheme_of_work_id, ", model.validation_errors:", model.validation_errors)
        redirect_to_url = reverse('schemesofwork.edit', args=[scheme_of_work_id])

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
def delete_unpublished(request):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_schemeofwork.delete_unpublished(db, request.user.id)

    return HttpResponseRedirect(redirect_to_url)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
def delete(request, scheme_of_work_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_schemeofwork.delete(db, request.user.id, 0)

    return HttpResponseRedirect(redirect_to_url)