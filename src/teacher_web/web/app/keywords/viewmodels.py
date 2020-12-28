import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class KeywordGetAllListViewModel(BaseViewModel):
    
    def __init__(self, db, request, scheme_of_work_id, auth_user):
        
        self.model = []
        self.auth_user = auth_user
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.schemeofwork_options = []
        
        try:
            # get model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
            #248 Http404
            if scheme_of_work_id > 0:
                if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                    self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)


            self.schemeofwork_options = SchemeOfWorkModel.get_options(self.db, self.auth_user)  

            # get model
            data = Model.get_all(db, scheme_of_work_id, 0, auth_user)
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
            "scheme_of_work": self.scheme_of_work,
            "keywords": self.model,
            "schemeofwork_options": self.schemeofwork_options
        }
        
        return ViewModel(self.scheme_of_work.name, self.scheme_of_work.name, self.scheme_of_work.description, data=data, active_model=self.scheme_of_work, error_message=self.error_message)


class KeywordGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, keyword_id, scheme_of_work_id, auth_user):

        self.model = None
        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id

        try:
            # get model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, scheme_of_work_id, auth_user)

            #248 Http404
            if scheme_of_work_id > 0:
                if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                    self.on_not_found(self.scheme_of_work, scheme_of_work_id)
            
            # get model
            model = Model.get_model(self.db, keyword_id, 0, scheme_of_work_id, auth_user)
            
            #299 Http404
            if model is None or model.is_from_db == False:
                self.on_not_found(model, keyword_id, scheme_of_work_id) 
            
            #253 check user id
            self.schemeofwork_options = SchemeOfWorkModel.get_options(self.db, self.auth_user) 

            self.model = model

        except Http404 as e:
            raise e

        except Exception as e:
            self.error_message = repr(e)
            handle_log_exception(db, "An error occurred viewing keywords", e)
            #TODO: REMOVE swallow up and handle on form
            raise e


    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "schemeofwork": self.scheme_of_work,
            "keyword": self.model,
            "schemeofwork_options": self.schemeofwork_options
        }

        return ViewModel(self.scheme_of_work.name, self.scheme_of_work.name, self.scheme_of_work.description, data=data, active_model=self.scheme_of_work)
        

class KeywordSaveViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.model = data


    def execute(self, published):
        
        def get_term(model):
            return model.term

        # TODO: 299 get all_terms before validating
        self.model.all_terms = list(map(get_term, Model.get_options(self.db, self.model.scheme_of_work_id, self.auth_user, exclude_id = self.model.id)))

        self.model.validate()

        if self.model.is_valid == True or published == 2:
            data = Model.save(self.db, self.model, self.auth_user)
            self.model = data   
        else:
            handle_log_warning(self.db, "saving keyword", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class KeywordDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, lesson_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, lesson_id, auth_user)
        self.model = data


class KeywordPublishModelViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, auth_user):
        data = Model.publish_by_id(db, auth_user, keyword_id)
        self.model = data