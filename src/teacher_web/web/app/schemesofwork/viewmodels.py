import json
from rest_framework import serializers, status
from django.http.response import Http404
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.viewmodels.baseviewmodel import BaseViewModel


class SchemeOfWorkIndexViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, key_stage_id=0):
        self.model = []

        self.db = db
        # get model
        data = Model.get_all(self.db, auth_user, key_stage_id)
        self.model = data


class SchemeOfWorkGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.db = db
        # get model
        model = Model.get_model(self.db, scheme_of_work_id, auth_user)
        if model is None or model.is_from_db == False:
            self.on_not_found(model, scheme_of_work_id) 
        self.model = model


class SchemeOfWorkEditViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):

        self.db = db
        self.auth_user = auth_user

        # assign data directly to the model

        self.model = data


    def execute(self, published):
        self.model.validate()
        
        if self.model.is_valid == True:
            data = Model.save(self.db, self.model, published)
            self.model = data   
        else:
            #    raise Exception("Scheme of work is not valid! {}".format(self.model.validation_errors))
            handle_log_warning(self.db, "saving scheme of work", "scheme of work is not valid (id:{}, name:{}, validation_errors (count:{}).".format(self.model.id, self.model.name, len(self.model.validation_errors)))

        return self.model


class SchemeOfWorkDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, auth_user):
        data = Model.delete_unpublished(db, auth_user)
        self.model = data


class SchemeOfWorkPublishModelViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, auth_user):
        data = Model.publish_by_id(db, auth_user, scheme_of_work_id)
        self.model = data
