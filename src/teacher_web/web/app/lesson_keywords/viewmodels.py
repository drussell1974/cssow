import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.viewmodels.decorators.permissions import check_teacher_permission
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class LessonKeywordIndexViewModel(BaseViewModel):
    
    
    def __init__(self, db, request, lesson_id, scheme_of_work_id, auth_user):
        
        self.model = []
        self.auth_user = auth_user
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        self.lesson_options = []
        
        try:
            # get model
            self.lesson = LessonModel.get_model(self.db, self.lesson_id, self.scheme_of_work_id, self.auth_user)
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
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
            handle_log_exception(self.db, self.scheme_of_work_id, "An error occured viewing resources", e)
            self.error_message = repr(e)
            raise e

    def view(self):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id":self.lesson_id,
            "scheme_of_work": self.scheme_of_work,
            "lesson": self.lesson,
            "keywords": self.model,
            "lesson_options": self.lesson_options
        }
        
        return ViewModel(self.lesson.title, self.lesson.title, self.lesson.summary, data=data, active_model=self.lesson, error_message=self.error_message)


class LessonKeywordSelectViewModel(BaseViewModel):
    
    @check_teacher_permission(LESSON.EDITOR)
    def __init__(self, db, request, lesson_id, scheme_of_work_id, auth_user):
            
        self.auth_user = auth_user
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        

    def execute(self, request):
        self.model = Model(
            id_ = request.POST.get("lesson_id", 0),
            scheme_of_work_id=request.POST.get("scheme_of_work_id", 0))
        
        self.model.key_words = list(map(lambda x: Model(int(x)), request.POST.getlist("term")))
        
        try:
            LessonModel.save_keywords(self.db, self.model, self.auth_user)    
        except Exception as ex:
            self.error_message = ex
            handle_log_exception(self.db, self.scheme_of_work_id, "An error occurred saving lesson keywords", ex)
            

    def view(self, request):      

        def mark_as_selected(keyword):
            if keyword.id in list(map(lambda x : int(x.id), self.model.key_words)):
                keyword.selected = True
                keyword.belongs_to_lessons.append(self.lesson_id)
            return keyword

        try:
            # get model
            self.model = LessonModel.get_model(self.db, self.lesson_id, self.scheme_of_work_id, self.auth_user)
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
            #248 Http404
            if self.lesson_id > 0:
                if self.model is None or self.model.is_from_db == False:
                    self.on_not_found(self.model, self.lesson_id, self.scheme_of_work_id)

            self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  
            
            self.keyword_options = list(map(mark_as_selected, self.scheme_of_work.key_words))
            
        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, self.scheme_of_work_id, "An error occured viewing resources", e)
            self.error_message = repr(e)
            raise e

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "lesson_id":self.lesson_id,
            "scheme_of_work": self.scheme_of_work,
            "lesson": self.model,
            "keywords": self.scheme_of_work.key_words,
            "lesson_options": self.lesson_options,
            "keyword_options": self.keyword_options
        }
        
        return ViewModel(self.model.title, self.model.title, "Select keywords for {}".format(self.model.title), data=data, active_model=self.model, error_message=self.error_message)


class LessonKeywordGetModelViewModel(BaseViewModel):
    
    @check_teacher_permission(LESSON.VIEWER)
    def __init__(self, db, keyword_id, lesson_id, scheme_of_work_id, auth_user):

        self.model = None
        self.db = db
        self.auth_user = auth_user
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id

        try:
            # get model
            self.lesson = LessonModel.get_model(self.db, lesson_id, scheme_of_work_id, auth_user)

            #248 Http404
            if lesson_id > 0:
                if self.lesson is None or self.lesson.is_from_db == False:
                    self.on_not_found(self.lesson, lesson_id, scheme_of_work_id)
            
            # get model
            model = Model.get_model(self.db, keyword_id, scheme_of_work_id, auth_user)
            
            #299 Http404 on keyword (also ensure keyword belongs to lesson)
            if model is None or model.is_from_db == False:
                self.on_not_found(model, keyword_id, lesson_id, scheme_of_work_id) 
            
            #253 check user id
            self.lesson_options = LessonModel.get_options(self.db, self.scheme_of_work_id, self.auth_user)  

            self.model = model

        except Http404 as e:
            raise e

        except Exception as e:
            self.error_message = repr(e)
            handle_log_exception(db, scheme_of_work_id, "An error occurred viewing keywords", e)
            #TODO: REMOVE swallow up and handle on form
            raise e


    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "lesson_id": self.lesson_id,
            "lesson": self.lesson,
            "schemeofwork": self.scheme_of_work,
            "keyword": self.model,
            "lesson_options": self.lesson_options
        }

        return ViewModel(self.lesson.title, self.lesson.title, self.lesson.summary, data=data, active_model=self.lesson)
        

class LessonKeywordSaveViewModel(BaseViewModel):

    @check_teacher_permission(LESSON.EDITOR)
    def __init__(self, db, scheme_of_work_id, model, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.model = model


    def execute(self, published):

        def get_term(record):
            return record.term

        # 299 get all_terms before validating (exluding current term)
        self.model.all_terms = list(map(get_term, Model.get_options(self.db, self.model.scheme_of_work_id, self.auth_user, exclude_id = self.model.id)))
        
        self.model.validate()

        if self.model.is_valid == True or published == 2:
            data = Model.save(self.db, self.model, self.auth_user)
            self.model = data   
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving keyword", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class LessonKeywordDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user)
        self.model = data


class LessonKeywordPublishModelViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, auth_user):
        data = Model.publish_by_id(db, auth_user, keyword_id)
        self.model = data
