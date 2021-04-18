import json
from django.http import Http404
from django.urls import reverse
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
#from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_topic import TopicModel
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class TopicIndexViewModel(BaseViewModel):
    
    def __init__(self, db, request, auth_ctx):
        
        self.model = []
        self.db = db
        self.request = request
        #self.institute_id = auth_ctx.institute_id
        #self.department_id = auth_ctx.department_id
        self.department = auth_ctx.department
        self.auth_ctx = auth_ctx
        
        try:
            
            # get model
            self.model = TopicModel.get_all(self.db, self.auth_ctx)

            #self.model = self.group_and_sort(data).items

        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, self.auth_ctx.department_id, "An error occured viewing topics", e)
            self.error_message = repr(e)
            raise e

    def view(self):

        data = {
            "department": self.auth_ctx.department,
            "topics": self.model
        }

        return ViewModel(self.department.name, self.department.name, "Topics", ctx=self.auth_ctx, data=data, active_model=self.department, error_message=self.error_message)


class TopicEditViewModel(BaseViewModel):

    def __init__(self, db, request, auth_ctx, topic_id = 0):

        self.db = db
        self.request = request
        self.auth_ctx = auth_ctx
        self.department = auth_ctx.department
        self.topic_id = topic_id
        

    def view(self):

        self.model = TopicModel(0, "", self.auth_ctx)
        
        if self.topic_id > 0:
            self.model = TopicModel.get_model(self.db, self.topic_id, self.auth_ctx)

        # topic options TODO: allow sub-topics
        self.topic_options = TopicModel.get_options(self.db, lvl=1, auth_ctx=self.auth_ctx)

        # view data
        data = {
            "topic_options": self.topic_options,
            "model": self.model,
        }
        
        return ViewModel("", self.department.name, self.model.name if len(self.model.name) != 0 else "Create new topic", ctx=self.auth_ctx, data=data, active_model=self.model, stack_trace=self.stack_trace, error_message=self.error_message, alert_message=self.alert_message)


    def execute(self, published=STATE.PUBLISH):
        
        self.model = TopicModel(0, "", self.auth_ctx)
        
        if self.topic_id > 0:
            self.model = TopicModel.get_model(self.db, self.topic_id, auth_ctx=self.auth_ctx)
        
        self.model.name = self.request.POST["name"]
        self.model.department_id = self.request.POST["department_id"]
        self.model.published = STATE.parse(self.request.POST["published"])
        self.model.parent_id = self.request.POST["parent_id"]

        self.model.validate()
        
        if self.model.is_valid == True or published == STATE.DELETE:
            data = TopicModel.save(self.db, self.model, auth_ctx=self.auth_ctx)
            
            self.on_post_complete(saved=True)

            self.model = data
        else:
            self.alert_message = "validation errors %s" % self.model.validation_errors
            handle_log_warning(self.db, self.topic_id, "saving topic", "topic is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

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