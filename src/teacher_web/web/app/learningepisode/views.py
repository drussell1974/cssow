from django.shortcuts import render
from django.db import connection as db
from shared.view_model import ViewModel
from cssow.models import cls_learningepisode, cls_schemeofwork

# Create your views here.        
def index(request, scheme_of_work_id):
    
    # TODO: get name from id in api call
    scheme_of_work_name = cls_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    lessons = cls_learningepisode.get_all(db, scheme_of_work_id, auth_user=request.user.id)
    schemeofwork_options = cls_schemeofwork.get_options(db, auth_user=request.user.id)
    
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("", scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "learningepisodes/index.html", view_model.content)

def new(request, scheme_of_work_id):
    ''' Create a new Learning Episode '''
    
    data = {
        "scheme_of_work_id":scheme_of_work_id
    }
    
    view_model = ViewModel("", "A-Level Computer Science", "Create", data=data)
    
    return render(request, "learningepisodes/edit.html", view_model.content)


def edit(request, scheme_of_work_id, learning_episode_id):
    ''' Edit the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Edit")
    
    return render(request, "learningepisodes/edit.html", view_model.content)

    
def copy(request, scheme_of_work_id, learning_episode_id):
    ''' Copy the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Copy")
    
    return render(request, "learningepisodes/edit.html", view_model.content)


def publish(request, scheme_of_work_id, learning_episode_id):
    ''' Publish the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Publish")
    # TODO: redirect
    return render(request, "learningepisodes/edit.html", view_model.content)


def delete(request, scheme_of_work_id, learning_episode_id):
    ''' Delete the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Delete")
    # TODO: redirect
    return render(request, "learningepisodes/edit.html", view_model.content)

    
def lessonplan(request, scheme_of_work_id, learning_episode_id):
    ''' Display the lesson plan '''

    view_model = ViewModel("", "", "lesson plan")
    
    return render(request, "learningepisodes/lessonplan.html", view_model.content)

    
def whiteboard(request, scheme_of_work_id, learning_episode_id):
    ''' Display the lesson plan on the whiteboard '''
    
    view_model = ViewModel("", "", "whiteboard")
    
    return render(request, "learningepisodes/whiteboard_view.html", view_model.content)