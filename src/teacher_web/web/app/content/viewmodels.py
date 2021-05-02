import json
from datetime import datetime
from rest_framework import serializers, status
from django.http import Http404
from django.urls import reverse
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.enums.publlished import STATE
from shared.models.cls_content import ContentModel as Model
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class ContentIndexViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        """ determine and action request """
        self.auth_user = auth_user
        
        # TODO: #323 call read only model
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_user)

        if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
            self.on_not_found(self.scheme_of_work, scheme_of_work_id) 

        self.scheme_of_work_options = SchemeOfWorkModel.get_options(db, auth_user)

        # get model
        self.model = Model.get_all(db, self.scheme_of_work.id, self.scheme_of_work.key_stage_id, auth_user)
        

    def view(self, request):
        """ return View """

        data = {
            "scheme_of_work_id": self.scheme_of_work.id,
            "curriculum_content": self.model,
            "schemeofwork_options": self.scheme_of_work_options
        }

        return ViewModel(request, "", self.scheme_of_work.name, "Scheme of work", content_heading="Curriculum", ctx=self.auth_user, data=data)
        

class ContentEditViewModel(BaseViewModel):
    
    is_content_ready = False
    error_message = ""

    def __init__(self, db, request, scheme_of_work_id, content_id, auth_user, wizard=None):
        
        self.db = db
        self.scheme_of_work_id = scheme_of_work_id
        self.content_id = content_id
        self.auth_user = auth_user
        self.wizard = wizard

        # TODO: #323 call read only model
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, self.auth_user)
        #248 check associated schemeofwork 
        if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
            self.on_not_found(self.scheme_of_work, content_id, scheme_of_work_id)

        if request.method == "GET":

            if content_id > 0:
                model = Model.get_model(self.db, content_id, scheme_of_work_id, self.auth_user)
                #248 check existing instance exists
                if model is None or model.is_from_db == False: 
                    self.on_not_found(self.scheme_of_work, content_id, scheme_of_work_id)
                self.model = model
            else:
                self.model = Model(
                    id_=0, 
                    description="", 
                    key_stage_id=self.scheme_of_work.key_stage_id,
                    created = datetime.now(),
                    #253 check user id
                    created_by_id = auth_user)

        elif request.method == "POST":
            
            published_state = STATE.parse(request.POST["published"])

            self.model = Model().from_post(request.POST)

            self.model.validate()
            
            if self.model.is_valid == True or published_state == STATE.DELETE:
                # save to database
                try:
                        
                    data = Model.save(self.db, self.model, self.auth_user, published_state)
                    self.model = data

                    self.is_content_ready = True   
                except Exception as e:
                    # TODO: show error message for custom exception
                    self.error_message = repr(e)
            else:
                handle_log_warning(self.db, scheme_of_work_id, "saving resource", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))


    def view(self, request):
        
        #if self.content_id > 0 and self.model is None:            
        #    self.on_not_found(self.model, self.content_id) 

        self.key_stage_options = KeyStageModel.get_options(self.db, self.auth_user)

        data = {
            "scheme_of_work_id":self.scheme_of_work.id,
            "key_stage_id":self.scheme_of_work.key_stage_id,
            "content_id":self.content_id,
            "model":self.model
        }
        
        return ViewModel(request, "", self.scheme_of_work.name, "Scheme of work", content_heading="Curriculum", ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, wizard=self.wizard)


class ContentDeleteUnpublishedViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, scheme_of_work_id):
        self.model = Model.delete_unpublished(db, auth_user=auth_user, scheme_of_work_id=scheme_of_work_id)
        
