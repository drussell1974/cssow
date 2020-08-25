import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_resource import ResourceModel as Model
from shared.viewmodels.baseviewmodel import BaseViewModel


class ResourceGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user):
        
        self.model = []
        
        # get model
        data = Model.get_all(db, lesson_id, scheme_of_work_id, auth_user)
        self.model = data


class ResourceGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, resource_id, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.model = None
        self.db = db
        
        # get model
        model = Model.get_model(self.db, resource_id, lesson_id, scheme_of_work_id, auth_user)
        if model is not None and Model.is_markdown(model):
            model.page_uri = reverse("api.resource.markdown", args=[scheme_of_work_id, lesson_id, resource_id, model.md_document_name]) 

        if model is None or model.is_from_db == False: 
            self.on_not_found(model, resource_id, lesson_id, scheme_of_work_id) 

        self.model = model


class ResourceSaveViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.model = data


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True or published == 2:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            handle_log_warning(self.db, "saving resource", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model

