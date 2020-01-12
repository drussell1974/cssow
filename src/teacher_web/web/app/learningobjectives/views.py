from django.db import connection as db
from django.shortcuts import render

from shared.view_model import ViewModel
from cssow.models import cls_lesson, cls_learningobjective


def index(request, scheme_of_work_id, lesson_id):

    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)
    learning_objectives = cls_learningobjective.get_all(db, lesson_id, request.user.id)
    
    lesson_options = cls_lesson.get_options(db, scheme_of_work_id, request.user.id)  
    
    #TODO: create view_learningepisiode_options: remove this line

    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "lesson_id":int(lesson_id),
        "lesson": lesson,
        "learning_objectives": learning_objectives,
        "lesson_options": lesson_options,
    }

    view_model = ViewModel("", lesson["title"], lesson["summary"], data=data)
    
    return render(request, "learningobjectives/index.html", view_model.content)
