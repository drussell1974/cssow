from django.shortcuts import render
from django.db import connection as db
from django.http import HttpResponse

from cssow.models import cls_schemeofwork
from shared.view_model import ViewModel

# Create your views here.
def index(request):

    # get the schemes of work
    latest_schemes_of_work = cls_schemeofwork.get_latest_schemes_of_work(db, top = 5)
    
    # TODO: use shared.ViewModel
    '''context = ViewModel(
        "", 
        "Teach Computer Science", 
        "Computing Schemes of Work across all key stages", 
        data=latest_schemes_of_work)'''

    context = {
        "page_title": "Dave Russell - Teach Computer Science",
        "content": {
            "main_heading":"Teach Computer Science",
            "sub_heading":"Computing Schemes of Work across all key stages",
            "latest_schemes_of_work": latest_schemes_of_work
        },
        "auth": {
            "user":False,
            "settings": {
                "actions_disabled":["register", "retrieve_password"],
            }
        },
        "session": {
            "alert_message":None
        }

    }

    return render(request, "default/index.html", context)
