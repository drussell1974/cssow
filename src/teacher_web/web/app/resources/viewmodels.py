import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_lesson import LessonModel
from shared.models.cls_resource import ResourceModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.viewmodels.decorators.permissions import check_teacher_permission
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class ResourceIndexViewModel(BaseViewModel):
    
    @check_teacher_permission(LESSON.VIEW)
    def __init__(self, db, request, lesson_id, scheme_of_work_id, auth_user):
        
        self.model = []
        self.auth_user = auth_user
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        self.lesson_options = []
        
        try:
            self.lesson = LessonModel.get_model(self.db, self.lesson_id, self.scheme_of_work_id, self.auth_user)
            # get model
            
            #248 Http404
            if self.lesson_id > 0:
                if self.lesson is None or self.lesson.is_from_db == False:
                    self.on_not_found(self.lesson, self.lesson_id, self.scheme_of_work_id)


            self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

            # get model
            data = Model.get_all(db, scheme_of_work_id, lesson_id, auth_user)
            self.model = data

        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, "An error occured viewing resources", e)
            self.error_message = repr(e)
            raise e

    def view(self):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id":self.lesson_id,
            "lesson": self.lesson,
            "resources": self.model,
            "lesson_options": self.lesson_options
        }

        return ViewModel(self.lesson.title, self.lesson.title, self.lesson.summary, data=data, active_model=self.lesson, error_message=self.error_message)






class ResourceGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, resource_id, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):

        self.model = None
        self.db = db
        self.auth_user = auth_user
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id

        try:
            # get model
            self.lesson = LessonModel.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)
            #248 Http404
            if lesson_id > 0:
                if self.lesson is None or self.lesson.is_from_db == False:
                    self.on_not_found(self.lesson, lesson_id, scheme_of_work_id)

            # get model
            model = Model.get_model(self.db, resource_id, lesson_id, scheme_of_work_id, auth_user)
            if model is not None and Model.is_markdown(model):
                model.page_uri = reverse("api.resource.markdown", args=[scheme_of_work_id, lesson_id, resource_id, model.md_document_name]) 

            if model is None or model.is_from_db == False:
                self.on_not_found(model, resource_id, lesson_id, scheme_of_work_id) 
            
            #253 check user id
            self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

            self.model = model

        except Http404 as e:
            raise e

        except Exception as e:
            self.error_message = repr(e)
            handle_log_exception(db, "An error occurred viewing resources", e)
            #TODO: REMOVE swallow up and handle on form
            raise e


    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "lesson_id": self.lesson_id,
            "lesson": self.lesson,
            "resources": self.model,
            "lesson_options": self.lesson_options
        }

        return ViewModel(self.lesson.title, self.lesson.title, self.lesson.summary, data=data, active_model=self.lesson)
        


class ResourceSaveViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, model, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        self.model = model


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True or published == 2:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            handle_log_warning(self.db, "saving resource", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model

