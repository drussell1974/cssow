from django.shortcuts import render
from django.http import HttpResponse

from cssow.models import cls_schemeofwork

# Create your views here.
def index(request):

    # get the schemes of work
    latest_schemes_of_work = cls_schemeofwork.get_latest_schemes_of_work(None, top = 5)
 
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
                "actions_disabled":True
            }
        },
        "session": {
            "alert_message":None
        }

    }

    return render(request, "default/index.html", context)