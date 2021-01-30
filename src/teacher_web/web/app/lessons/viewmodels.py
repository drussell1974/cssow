import json
from django.http import Http404
from rest_framework import serializers, status
from shared.models.core.basemodel import try_int
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel as Model, LessonFilter
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from app.default.viewmodels import KeywordSaveViewModel


class LessonIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, scheme_of_work_id, page, pagesize, pagesize_options, keyword_search, auth_user):
        
        data = []

        self.model = []
        self.db = db
        self.scheme_of_work_id = scheme_of_work_id
        #page_direction = 0
        # create pager
        self.search_criteria = LessonFilter(keyword_search, pagesize_options, page, pagesize, 0)
    
        try:
            # name to appear
            self.scheme_of_work_name = SchemeOfWorkModel.get_schemeofwork_name_only(db, scheme_of_work_id, auth_user)
            if self.scheme_of_work_name is None or self.scheme_of_work_name == "":
                self.on_not_found(self.scheme_of_work_name, scheme_of_work_id)

            # side menu options
            self.schemeofwork_options = SchemeOfWorkModel.get_options(db, auth_user=auth_user)
            self.model = data
            
            # get pager from POST 

            if request.method == "POST":
                self.search_criteria.pager(request.POST["page"], request.POST["page_direction"])
                self.search_criteria.pagesize = try_int(request.POST["pagesize"], return_value=pagesize)
                
            # get list of lessons
            self.model = Model.get_filtered(self.db, scheme_of_work_id, self.search_criteria, auth_user)

        except Http404 as notfound:
            raise notfound        
        except Exception as e:
            self.error_message = repr(e)
            handle_log_exception(db, scheme_of_work_id, "Error initialising LessonIndexViewModel", e)
            

    def view(self):

        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "schemeofwork_options": self.schemeofwork_options,
            "lessons": self.model,
            "topic_name": "",
            "search_criteria": self.search_criteria,
        }

        return ViewModel(self.scheme_of_work_name, self.scheme_of_work_name, "Lessons", data=data, error_message=self.error_message)


class LessonGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = Model.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)

        #248 Http404
        if lesson_id > 0:
            if model is None or model.is_from_db == False:
                self.on_not_found(model, lesson_id, scheme_of_work_id)

        self.model = model


class LessonWhiteboardViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = Model.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)

        #248 Http404
        if lesson_id > 0:
            if model is None or model.is_from_db == False:
                self.on_not_found(model, lesson_id, scheme_of_work_id)

        self.model = model


class LessonEditViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, model, auth_user):
        
        self.db = db
        self.auth_user = auth_user
        self.model = model
        self.scheme_of_work_id = scheme_of_work_id


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving lesson", "lesson is not valid (id:{}, title:{}, validation_errors (count:{}).".format(self.model.id, self.model.title, len(self.model.validation_errors)))

        return self.model


class LessonPublishViewModel(BaseViewModel):


    def __init__(self, db, auth_user, lesson_id, scheme_of_work_id):
        self.model = Model.publish(db, auth_user, lesson_id, scheme_of_work_id)
    

class LessonDeleteViewModel(BaseViewModel):

    def __init__(self, db, auth_user, lesson_id):
        self.model = Model.delete(db, auth_user, lesson_id)


class LessonDeleteUnpublishedViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, scheme_of_work_id):
        self.model = Model.delete_unpublished(db, auth_user=auth_user, scheme_of_work_id=scheme_of_work_id)
