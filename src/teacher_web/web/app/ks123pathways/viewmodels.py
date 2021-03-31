import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
from shared.models.cls_topic import TopicModel
from shared.models.cls_year import YearModel
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


class KS123PathwayEditViewModel(BaseViewModel):

    def __init__(self, db, request, auth_ctx, pathway_item_id = 0):

        self.db = db
        self.request = request
        self.auth_ctx = auth_ctx
        self.department = auth_ctx.department
        self.pathway_item_id = pathway_item_id
        

    def view(self):

        self.model = Model(0, "", self.auth_ctx)
        
        if self.pathway_item_id > 0:
            self.model = Model.get_model(self.db, self.pathway_item_id, auth_ctx=self.auth_ctx)
        
        # topic options
        self.topic_options = TopicModel.get_options(self.db, lvl=1, auth_user=self.auth_ctx)

        # view data
        data = {
            "topic_options": self.topic_options,
            "year_options": self.model.start_study_in_year_options,
            "model": self.model
        }
        
        return ViewModel("", self.department.name, self.model.objective if len(self.model.objective) != 0 else "Create new pathway objective", ctx=self.auth_ctx, data=data, active_model=self.model, stack_trace=self.stack_trace, error_message=self.error_message, alert_message=self.alert_message)


    def execute(self, published=STATE.PUBLISH):
        
        self.model = Model(0, "", self.auth_ctx)
        
        if self.pathway_item_id > 0:
            self.model = Model.get_model(self.db, self.pathway_item_id, auth_ctx=self.auth_ctx)
        
        self.model.objective = self.request.POST["objective"]
        self.model.topic_id = self.request.POST["topic_id"]
        self.model.year_id = self.request.POST["year_id"]

        self.model.validate()
        
        if self.model.is_valid == True or published == STATE.DELETE:
            data = Model.save(self.db, self.model, auth_ctx=self.auth_ctx)
            self.model = data
        else:
            handle_log_warning(self.db, self.pathway_item_id, "saving pathway", "pathway is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model

"""
class LessonKeywordDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, lesson_id=lesson_id, auth_user=auth_user)
        self.model = data


class LessonKeywordPublishModelViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, auth_user):
        data = Model.publish_by_id(db, auth_user, keyword_id)
        self.model = data
"""