from django.shortcuts import render
from django.db import connection as db
from shared.view_model import ViewModel
from cssow.models import cls_learningepisode

# Create your views here.        
def index(request, scheme_of_work_id):
    
    lessons = cls_learningepisode.get_all(db, scheme_of_work_id, auth_user=request.user.id, enable_logging=True)
    schemeofwork_options = [] #cls_schemeofwork.get_options(db, auth_user=request.user.id)
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("", "A-Level Computer Science", "Lessons", data=data)
    
    return render(request, "learningepisodes/index.html", view_model.content)

def new(request, scheme_of_work_id):
    data = {
        "scheme_of_work_id":scheme_of_work_id
    }
    
    view_model = ViewModel("", "A-Level Computer Science", "Create", data=data)
    
    return render(request, "learningepisodes/new.html", view_model.content)