from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse

from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess
from shared.view_model import ViewModel

# Create your views here.
def index(request):

    # get the schemes of work
    latest_schemes_of_work = SchemeOfWorkDataAccess.get_latest_schemes_of_work(db, top = 5)
    
    data = {
        "latest_schemes_of_work":latest_schemes_of_work
    }

    view_model = ViewModel("", "Teach Computer Science", "Computing Schemes of Work across all key stages", data=data)

    return render(request, "default/index.html", view_model.content)
