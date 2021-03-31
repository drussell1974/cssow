from datetime import datetime
import json
import traceback
from rest_framework import serializers, status
from django.http.response import Http404
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_department import DepartmentModel
from shared.models.cls_examboard import ExamBoardModel
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class SchemeOfWorkIndexViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, key_stage_id=0):
        self.model = []
        self.db = db
        self.auth_user = auth_user
        # get model

        data = Model.get_all(self.db, auth_user, key_stage_id)
        self.model = data


    def view(self):

        data = {
            "schemes_of_work":self.model
        }
        
        return ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", ctx=self.auth_user, data=data)


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
                

    def view(self):
        
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

        return ViewModel("", "Schemes of Work", self.model.name if len(self.model.name) != 0 else "Create new scheme of work", ctx=self.auth_user, data=data, active_model=self.model, stack_trace=self.stack_trace, error_message=self.error_message, alert_message=self.alert_message, delete_dialog_message=delete_message, wizard=self.wizard)

 
class SchemeOfWorkDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        
        data = Model.delete_unpublished(db, auth_user)
        self.model = data


class SchemeOfWorkPublishModelViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, auth_user):
        data = Model.publish_by_id(db, auth_user, scheme_of_work_id)
        self.model = data
