from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from shared.view_model import ViewModel
from cssow.models import cls_lesson, cls_schemeofwork, cls_ks123pathway, cls_learningobjective, cls_topic, cls_year
from cssow.models.core import validation_helper
from datetime import datetime

# Create your views here.        
def index(request, scheme_of_work_id):
    
    scheme_of_work_name = cls_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    lessons = cls_lesson.get_all(db, scheme_of_work_id, auth_user=request.user.id)
    schemeofwork_options = cls_schemeofwork.get_options(db, auth_user=request.user.id)
    
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("", scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)


def new(request, scheme_of_work_id):
    ''' Create a new Learning Episode '''
    
    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)
    
    lesson = cls_lesson.get_model(db, 0, request.user.id)
    lesson["key_stage_id"] = scheme_of_work.key_stage_id
    lesson["scheme_of_work_id"] = scheme_of_work.id
    
    year_options = cls_year.get_options(db, scheme_of_work.key_stage_id)
    topic_options = cls_topic.get_options(db, lvl=1)

    data = {
        "scheme_of_work_id": int(scheme_of_work_id),
        "lesson_id": int(lesson["id"]),
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": 0, 
        "year_options": year_options,
        "selected_year_id": 0,
        "lesson": lesson
    }
    
    view_model = ViewModel("", scheme_of_work.name, "New", data=data)
    
    return render(request, "lessons/edit.html", view_model.content)


def edit(request, scheme_of_work_id, lesson_id):
    ''' Edit the Learning Episode '''
    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)
    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)
    year_options = cls_year.get_options(db, scheme_of_work.key_stage_id)
    topic_options = cls_topic.get_options(db, lvl=1)

    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson["id"],
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "year_options": year_options,
        "lesson": lesson
    }
    
    view_model = ViewModel("Dave Russell - Computer Science", "A-Level Computer Science", "Edit: {}".format(lesson["title"]), data=data)
    
    return render(request, "lessons/edit.html", view_model.content)

    
def copy(request, scheme_of_work_id, lesson_id):
    ''' Copy the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Copy")
    
    return render(request, "lessons/edit.html", view_model.content)


def publish(request, scheme_of_work_id, lesson_id):
    ''' Publish the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Publish")
    # TODO: redirect
    return render(request, "lessons/edit.html", view_model.content)


def delete(request, scheme_of_work_id, lesson_id):
    ''' Delete the Learning Episode '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Delete")
    # TODO: redirect
    return render(request, "lessons/edit.html", view_model.content)

    
def lessonplan(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan '''

    view_model = ViewModel("", "", "lesson plan")
    
    return render(request, "lessons/lessonplan.html", view_model.content)

    
def whiteboard(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan on the whiteboard '''
    
    view_model = ViewModel("", "", "whiteboard")
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


def save(request, scheme_of_work_id, lesson_id):
    """ save_item non-view action """
    print("views.lesson.save:- calling...:")

    published = int(request.POST["published"] if request.POST["published"] is not None else 1)
    print("views.lesson.save:- published:", published)

    model = cls_lesson.LessonModel(
        id_ = request.POST["id"],
        orig_id = int(request.POST["orig_id"]),
        title = request.POST["title"],
        order_of_delivery_id = request.POST["order_of_delivery_id"],
        scheme_of_work_id = request.POST["scheme_of_work_id"],
        topic_id = request.POST["topic_id"],
        related_topic_ids = request.POST["related_topic_ids"],
        key_stage_id= request.POST["key_stage_id"],
        year_id = request.POST["year_id"],
        key_words = request.POST["key_words"],
        summary = request.POST["summary"],
        created = datetime.now(),
        created_by_id = request.user.id
    )

    '''
    # ensure pathway_objective_ids is assigned as a list
    if type(request.POST["pathway_objective_ids) is str:
        model.pathway_objective_ids = []
        model.pathway_objective_ids.append(request.POST["pathway_objective_ids"])
    else:
        model.pathway_objective_ids = request.POST["pathway_objective_ids"]

    # ensure pathway_ks123_ids is assigned as a list
    if type(request.POST["pathway_ks123_ids"]) is str:
        model.pathway_ks123_ids = []
        model.pathway_ks123_ids.append(request.POST["pathway_ks123_ids"])
    else:
        model.pathway_ks123_ids = request.POST["pathway_ks123_ids"]
    '''
    
    # reset id if a copy
    if int(request.POST["orig_id"]) > 0:
        print("views.lesson.save:- is a copy of ", request.POST["orig_id"])
        model.id = 0

    print("views.lesson.save:- validating...") 
    model.validate()
    print("views.lesson.save:- model.is_valid:", model.is_valid) 

    if model.is_valid == True:
        print("views.lesson.save:- saving... ") 
        ' save the lesson '
        model = cls_lesson.save(db, model, published)
        print("views.lesson.save:- saved!")
        print("views.lesson.save:- model.id:", model.id) 

        ' save keywords '
        #db_keyword.save_keywords_only(db, model.key_words.split(','))
        
        print("views.lesson.save:- redirecting...")

        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id, model.id))
        print("views.lesson.save:- redirect_to_url:", redirect_to_url)
    else:
        print("views.lesson.save:- redirecting back to page") 
        """ redirect back to page and show message """
        print("views.lesson.save:- validation_errors:", model.validation_errors)
        request.session.alert_message = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        #if request.env.http_referer:
        #    redirect_to_url = request.env.http_referer
        redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id,lesson_id))

    print("views.lesson.save:- completed!")
    return HttpResponseRedirect(redirect_to_url)
