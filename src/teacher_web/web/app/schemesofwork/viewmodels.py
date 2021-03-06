from datetime import datetime
import json
import traceback
from rest_framework import serializers, status
from django.conf import settings
from django.http.response import Http404
from django.urls import reverse
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning, handle_log_info
from shared.models.core.basemodel import try_int
from shared.models.cls_department import DepartmentModel
from shared.models.cls_examboard import ExamBoardModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_lesson_schedule import LessonScheduleModel
from shared.models.cls_notification import NotifyModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from app.default.viewmodels import DefaultIndexViewModel


class SchemeOfWorkIndexViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, key_stage_id=0):
        super().__init__(auth_user)
        
        self.model = []
        self.db = db
        self.auth_user = auth_user
        # get model

        data = Model.get_all(self.db, auth_user, key_stage_id)
        self.model = data


    def view(self, request):

        data = {
            "schemes_of_work":self.model
        }
        
        return ViewModel(request, "", self.auth_user.department.name, "Department", content_heading="Schemes of work", ctx=self.auth_user, data=data)


class SchemeOfWorkGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.db = db
        # get model
        model = Model.get_model(self.db, scheme_of_work_id, auth_user)
        if model is None or model.is_from_db == False:
            self.on_not_found(model, scheme_of_work_id) 
        self.model = model


class SchemeOfWorkEditViewModel(BaseViewModel):

    def __init__(self, db, request, scheme_of_work_id, auth_user, wizard=None):
        
        self.db = db
        self.auth_user = auth_user
        # new scheme of work 
        self.model = Model(id_=scheme_of_work_id, name="", study_duration=0, start_study_in_year=1, auth_user=auth_user)
        
        self.wizard = wizard

        if request.method == "GET" and self.model.id > 0:
            ## GET request from client ##
            getmodel_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user)

            self.model = getmodel_view.model
        
        elif request.method == "POST":
            ## POST back from client ##
            
            # create instance of model from request.vars
            self.model = Model(
                id_=request.POST.get("id", 0),
                name=request.POST.get("name", ""),
                description=request.POST.get("description", ""),
                exam_board_id=request.POST.get("exam_board_id", 0),
                key_stage_id=request.POST.get("key_stage_id", 0),
                study_duration = request.POST.get("study_duration", 0),
                start_study_in_year = request.POST.get("start_study_in_year", 1), # can be, e.g., 7 (Year7) for KS3, Year 10 for KS4
                created=datetime.now(), 
                created_by_id=self.auth_user.auth_user_id,
                auth_user=auth_user)
            
            try:
                
                #256 create the pathway options and return key_stage
                '''
                '''

                # save Scheme of work
                
                self.model.validate()
                    
                if self.model.is_valid == True:
                    published_state = STATE.parse(request.POST.get("published", "PUBLISH"))

                    data = Model.save(self.db, self.model, self.auth_user, published=published_state)

                    self.on_post_complete(True)
                    self.model = data
                else:
                    self.alert_message = "validation errors %s" % self.model.validation_errors 
                    handle_log_warning(self.db, scheme_of_work_id, "saving scheme of work", "scheme of work is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.name, len(self.model.validation_errors)))
                    
            except Exception as ex:
                # TODO: use this in other ViewModels
                self.on_exception(ex)
                handle_log_exception(db, scheme_of_work_id, "An error occurred processing scheme of work", ex)
                raise ex
                

    def view(self, request):
        
        # get options
        self.examboard_options = ExamBoardModel.get_options(self.db, self.auth_user)
        # keystage_options are templates templates
        self.keystage_options =  KeyStageModel.get_options(self.db, self.auth_user)
        self.department_options = DepartmentModel.get_options(self.db, self.auth_user)

        # view data
        data = {
            "scheme_of_work_id": self.model.id,
            "scheme_of_work": self.model,
            "examboard_options": self.examboard_options,
            "keystage_options": self.keystage_options,
            "department_options": self.department_options,
            "start_study_in_year_options": self.model.start_study_in_year_options
        }
        
        # build alert message to be displayed
        delete_message = "<p>'{display_name}' ({id}) will be deleted!<ul>".format(display_name=self.model.name, id=self.model.id)
        if self.model.number_of_lessons > 0:
            delete_message = delete_message + "<li>{number_of_lessons} lesson(s)</li>".format(number_of_lessons=self.model.number_of_lessons)
        if self.model.number_of_learning_objectives > 0:
            delete_message = delete_message + "<li>{number_of_learning_objectives} learning objective(s)</li>".format(number_of_learning_objectives=self.model.number_of_learning_objectives)
        if self.model.number_of_resources > 0:
            delete_message = delete_message + "<li>{number_of_resources} resource(s)</li>".format(number_of_resources=self.model.number_of_resources)
        delete_message = delete_message + "</ul>"

        return ViewModel(request, "", self.auth_user.department.name, "Department", content_heading="Scheme of work", ctx=self.auth_user, data=data, active_model=self.model, stack_trace=self.stack_trace, error_message=self.error_message, alert_message=self.alert_message, delete_dialog_message=delete_message, wizard=self.wizard)

 
class SchemeOfWorkDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        
        data = Model.delete_unpublished(db, auth_user)
        self.model = data


class SchemeOfWorkPublishModelViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, auth_user):
        data = Model.publish_by_id(db, auth_user, scheme_of_work_id)
        self.model = data

'''
class SchemeOfWorkScheduleViewModel(DefaultIndexViewModel):

    def __init__(self, db, request, institute_id, department_id, scheme_of_work_id, auth_user):
        super().__init__(db, 0, auth_user)
        self.scheme_of_work_id = scheme_of_work_id
        self.scheme_of_work = Model.get_model(db, id=scheme_of_work_id, auth_user=auth_user)
        
        # if not found then raise error
        if self.scheme_of_work_id > 0:
            if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)

        self.schemeofwork_options = Model.get_options(self.db, self.auth_user)  
        self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

        # get default from settings
        self.show_next_days = request.session.get("lesson_schedule.show_next_days", settings.PAGER["schedule"]["pagesize"])

        if request.method == "POST":
            # get show_next_days from POST or use default set above
            self.show_next_days = try_int(request.POST.get("show_next_days", self.show_next_days))
            request.session["lesson_schedule.show_next_days"] = self.show_next_days

        #lesson_id, scheme_of_work_id, auth_user
        data = LessonScheduleModel.get_all(db, lesson_id=0, scheme_of_work_id=scheme_of_work_id, show_next_days=self.show_next_days, auth_user=auth_user)
        self.model = data


    def view(self, request, main_heading, sub_heading):
        super().view(self.scheme_of_work.name, sub_heading)
        
        data = {
            "schemeofwork": self.scheme_of_work,
            "scheme_of_work_id": self.scheme_of_work_id,
            "schemeofwork_options": self.schemeofwork_options,
            "lesson_options": self.lesson_options,
            "schedules": self.model,
            "show_next_days": self.show_next_days,
            "days_to_show__options": settings.PAGER["schedule"]["pagesize_options"],
        }

        return ViewModel(request, "", main_heading, sub_heading, ctx=self.auth_user, data=data, active_model=self.scheme_of_work)

'''