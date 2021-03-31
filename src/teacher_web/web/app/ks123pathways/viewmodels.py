import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class KS123PathwayIndexViewModel(BaseViewModel):
    
    @classmethod
    def group_and_sort(cls, data):
        grouped_data = {}

        for row in data:
            if grouped_data.get(row.topic.name) == None:
                # create value as array if not already
                grouped_data[row.topic.name] = []
            # append row
            grouped_data[row.topic.name].append(row)

        return grouped_data

    
    def __init__(self, db, request, auth_ctx):
        
        self.model = []
        self.db = db
        self.request = request
        self.institute_id = auth_ctx.institute_id
        self.department_id = auth_ctx.department_id
        self.department = auth_ctx.department
        self.auth_ctx = auth_ctx
        self.lesson_options = []
        
        try:
            
            # get model
            data = Model.get_all(self.db, self.department_id, self.auth_ctx)

            self.model = self.group_and_sort(data).items

        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, self.department_id, "An error occured viewing pathways", e)
            self.error_message = repr(e)
            raise e

    def view(self):

        data = {
            "department": self.auth_ctx.department,
            "ks123pathway": self.model,
        }

        return ViewModel(self.department.name, self.department.name, "KS123 Pathways", ctx=self.auth_ctx, data=data, active_model=self.department, error_message=self.error_message)


"""
class LessonKeywordGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, keyword_id, lesson_id, scheme_of_work_id, auth_user):

        self.model = None
        self.db = db
        self.auth_user = auth_user
        self.lesson_id = lesson_id
        self.scheme_of_work_id = scheme_of_work_id

        try:
            # get model
            self.lesson = LessonModel.get_model(self.db, lesson_id, scheme_of_work_id, auth_user)

            # if not found then raise error
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
            # TODO: REMOVE swallow up and handle on form
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

        return ViewModel(self.lesson.title, self.lesson.title, self.lesson.summary, ctx=self.auth_user, data=data, active_model=self.lesson)
        

class LessonKeywordSaveViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, model, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.lesson_id = lesson_id
        self.model = model


    def execute(self, published):

        def get_term(record):
            return record.term

        # 299 get all_terms before validating (exluding current term)
        self.model.all_terms = list(map(get_term, Model.get_options(self.db, self.model.scheme_of_work_id, self.auth_user, exclude_id = self.model.id)))
        
        self.model.validate()

        if self.model.is_valid == True or published == STATE.DELETE:
            data = Model.save(self.db, self.model, lesson_id=self.lesson_id, auth_user=self.auth_user)
            self.model = data   
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving keyword", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class LessonKeywordDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_user)
        self.model = data


class LessonKeywordPublishModelViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, auth_user):
        data = Model.publish_by_id(db, auth_user, keyword_id)
        self.model = data
"""