from django.shortcuts import render

from shared.view_model import ViewModel

# Create your views here.
def index(request, scheme_of_work_id, learning_episode_id):
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "learning_episode_id":int(learning_episode_id),
        "lesson": {},
        "learning_objectives": []
    }

    view_model = ViewModel("", "", "", data=data)
    
    return render(request, "learningobjectives/index.html", view_model.content)

