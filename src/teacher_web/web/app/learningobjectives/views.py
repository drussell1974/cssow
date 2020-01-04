from django.db import connection as db
from django.shortcuts import render

from shared.view_model import ViewModel
from cssow.models import cls_learningepisode, cls_learningobjective


def index(request, scheme_of_work_id, learning_episode_id):

    learning_episode = cls_learningepisode.get_model(db, learning_episode_id, request.user.id)
    learning_objectives = cls_learningobjective.get_all(db, learning_episode_id, request.user.id)
    
    learning_episode_options = cls_learningepisode.get_options(db, scheme_of_work_id, request.user.id)  
    
    #TODO: create view_learningepisiode_options: remove this line

    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "learning_episode_id":int(learning_episode_id),
        "lesson": learning_episode,
        "learning_objectives": learning_objectives,
        "learning_episode_options": learning_episode_options,
    }

    view_model = ViewModel("", learning_episode["title"], learning_episode["summary"], data=data)
    
    return render(request, "learningobjectives/index.html", view_model.content)
