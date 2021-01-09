"""
View Models
"""
import io
from rest_framework import serializers, status
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning, handle_log_error
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.viewmodels.decorators.permissions import check_teacher_permission
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class SchemeOfWorkGetLatestViewModel(BaseViewModel):
    
    def __init__(self, db, top, auth_user):
        self.model = []
        self.db = db

        try:
            # get model
            data = SchemeOfWorkModel.get_latest_schemes_of_work(self.db, top=5, auth_user=auth_user)
            self.model = data
        except Exception as e:
            self.error_message = repr(e)


    def view(self, main_heading, sub_heading):

        data = {
            "latest_schemes_of_work":self.model
        }
        
        return ViewModel("", main_heading, sub_heading, data=data, error_message=self.error_message)


class TopicGetOptionsListViewModel(BaseViewModel):
    #TODO: #235 Rename to {ViewName}ViewModel
    def __init__(self, db, topic_id, auth_user, lvl=2):
        raise DeprecationWarning("no matching view")
        self.model = TopicModel.get_options(db, topic_id=topic_id, auth_user=auth_user, lvl=lvl)


class KeywordGetOptionsListViewModel(BaseViewModel):
    # TODO: #235 Depracate not a matching View
    def __init__(self, db, scheme_of_work_id, auth_user):
        raise DeprecationWarning("no matching view")
        self.model = KeywordModel.get_options(db, scheme_of_work_id, auth_user)


class KeywordGetAllListViewModel(BaseViewModel):
    #TODO: #235 Depracate not a matching View
    def __init__(self, db, scheme_of_work_id, auth_user):
        raise DeprecationWarning("no matching view")
        self.model = KeywordModel.get_all(db, scheme_of_work_id,  auth_user)


class KeywordGetModelViewModel(BaseViewModel):
    #TODO: #235 Depracate not a matching View
    def __init__(self, db, keyword_id, lesson_id, scheme_of_work_id, auth_user):
        raise DeprecationWarning("no matching view")
        self.db = db
        # get model
        data = KeywordModel.get_model(self.db, keyword_id, scheme_of_work_id, auth_user)
        self.model = data
        

class KeywordSaveViewModel(BaseViewModel):
    def __init__(self, db, model):
        self.db = db
        self.model = model


    def execute(self, auth_user, published=1):

        if type(self.model) is KeywordModel:
            
            self.model.validate()
            
            if self.model.is_valid == True:
                data = KeywordModel.save(self.db, self.model, auth_user)
                self.model = data
            else:
                handle_log_error(self.db, "saving keyword", "keyword not valid (keyword id:{}, term:'{}', definition:'{}', scheme_of_work_id:{}) validation_errors:{}".format(self.model.id, self.model.term, self.model.definition, self.model.scheme_of_work_id, self.model.validation_errors))
        else:
            raise AttributeError("Cannot save KeywordModel of type {}".format(type(self.model)))
        
        return self.model

