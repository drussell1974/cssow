from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse

from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess
from shared.view_model import ViewModel
from .viewmodels import SchemeOfWorkGetLatestViewModel

# Create your views here.
def index(request):

    # get the schemes of work
    latest_schemes_of_work__view = SchemeOfWorkGetLatestViewModel(db, top = 5, auth_user=request.user.id)
    
    data = {
        "latest_schemes_of_work":latest_schemes_of_work__view.model
    }

    view_model = ViewModel("", "Teach Computer Science", "Computing Schemes of Work across all key stages", data=data)

    return render(request, "default/index.html", view_model.content)
