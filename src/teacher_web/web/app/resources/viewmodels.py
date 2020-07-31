import json
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_resource import ResourceModel as Model, ResourceDataAccess as DataAccess
#from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel


class ResourceGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user):
        
        self.model = []
        
        # get model
        data = DataAccess.get_all(db, lesson_id, scheme_of_work_id, auth_user)
        self.model = data


class ResourceGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, resource_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        data = DataAccess.get_model(self.db, resource_id, scheme_of_work_id, auth_user)
        self.model = data


class ResourceSaveViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.model = data


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True or published == 2:
            data = DataAccess.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            #    raise Exception("Lesson is not valid! {}".format(self.model.validation_errors))
            handle_log_warning(self.db, "saving resource", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model

