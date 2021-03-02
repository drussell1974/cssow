import json
from django.http import Http404
from django.urls import reverse
from rest_framework import serializers, status
from shared.models.core.log_handlers import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.enums.publlished import STATE
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel


class KeywordGetAllListViewModel(BaseViewModel):
    
    def __init__(self, db, request, scheme_of_work_id, auth_user):
        
        self.model = []
        self.db = db
        self.request = request
        self.scheme_of_work_id = scheme_of_work_id
        self.auth_user = auth_user
        self.schemeofwork_options = []
        
        try:
            # get model
            # TODO: #323 call read only model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
            # if not found then raise error
            if scheme_of_work_id > 0:
                if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                    self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)


            self.schemeofwork_options = SchemeOfWorkModel.get_options(self.db, self.auth_user)  

            # get model
            data = Model.get_all(db, scheme_of_work_id, 0, auth_user)

            for kw in data:
                kw.belongs_to_lessons = LessonModel.get_by_keyword(db, kw.id, scheme_of_work_id, auth_user)

            self.model = data

        except Http404 as e:
            raise e

        except Exception as e:
            handle_log_exception(self.db, scheme_of_work_id, "An error occured viewing resources", e)
            self.error_message = repr(e)
            raise e


    def view(self):

        data = {
            "scheme_of_work_id": self.scheme_of_work_id,
            "scheme_of_work": self.scheme_of_work,
            "keywords": self.model,
            "schemeofwork_options": self.schemeofwork_options
        }
        
        return ViewModel(self.scheme_of_work.name, self.scheme_of_work.name, self.scheme_of_work.description, ctx=self.auth_user, data=data, active_model=self.scheme_of_work, error_message=self.error_message)


class KeywordGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, keyword_id, scheme_of_work_id, auth_user):

        self.model = None
        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id

        try:
            # get model
            # TODO: #323 call read only model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, scheme_of_work_id, auth_user)
            
            # if not found then raise error
            if scheme_of_work_id > 0:
                if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                    self.on_not_found(self.scheme_of_work, scheme_of_work_id)
            
            # get model
            model = Model.get_model(self.db, keyword_id, scheme_of_work_id, auth_user)

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
            handle_log_exception(db, scheme_of_work_id, "An error occurred viewing keywords", e)
            # TODO: REMOVE swallow up and handle on form
            raise e


    def view(self):
        
        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "schemeofwork": self.scheme_of_work,
            "keyword": self.model,
            "schemeofwork_options": self.schemeofwork_options
        }

        return ViewModel(self.scheme_of_work.name, self.scheme_of_work.name, self.scheme_of_work.description, ctx=self.auth_user, data=data, active_model=self.scheme_of_work)
        

class KeywordSaveViewModel(BaseViewModel):


    def __init__(self, db, scheme_of_work_id, model, auth_user):

        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.model = model


    def execute(self, published):
        
        def get_term(model):
            return model.term

        self.model.all_terms = list(map(get_term, Model.get_options(self.db, self.model.scheme_of_work_id, self.auth_user, exclude_id = self.model.id)))

        self.model.validate()

        if self.model.is_valid == True or published == STATE.DELETE:
            data = Model.save(self.db, self.model, self.auth_user)
            self.model = data   
        else:
            handle_log_warning(self.db, self.scheme_of_work_id, "saving keyword", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))

        return self.model


class KeywordDeleteUnpublishedViewModel(BaseViewModel):

    def __init__(self, db, scheme_of_work_id, auth_user):
        data = Model.delete_unpublished(db, scheme_of_work_id, auth_user)
        self.model = data


class KeywordPublishModelViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, auth_user):
        data = Model.publish_by_id(db, auth_user, keyword_id)
        self.model = data


class KeywordMergeViewModel(BaseViewModel):

    def __init__(self, db, keyword_id, scheme_of_work_id, auth_user):
        
        self.db = db
        self.auth_user = auth_user
        self.scheme_of_work_id = scheme_of_work_id
        self.keyword_id = keyword_id
        self.schemeofwork_options = []
        self.completed = False
        

    def execute(self, request):
        try:
            self.redirect_to_url = ""
            self.alert_message = "Duplicate keywords will be merged and deleted and definition lost. Click Merge to continue or click Cancel to return to the previous page."

            if request.method == "POST":
                published_state = STATE.parse(request.POST.get("published"))
                if published_state == STATE.DELETE:
                    # 303 execute merge
                    self.model = Model.merge_duplicates(self.db, self.keyword_id, self.scheme_of_work_id, self.auth_user)
                    self.alert_message = "deleted!"
                    
                if request.POST["next"] != None and request.POST["next"] != "":
                    self.redirect_to_url = request.POST["next"]
                else:
                    self.redirect_to_url = reverse('keyword.index', args=(self.scheme_of_work_id))
                
                self.redirect_to_url = "{}#{}".format(self.redirect_to_url, self.keyword_id) # jumps to merged keyword using bookmark in url
                
                # POST completed
                self.completed = True
                
                return

            # get model
            self.scheme_of_work = SchemeOfWorkModel.get_model(self.db, self.scheme_of_work_id, self.auth_user)
            
            self.schemeofwork_options = SchemeOfWorkModel.get_options(self.db, self.auth_user) 

            # if not found then raise error
            if self.scheme_of_work_id > 0:
                if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
                    self.on_not_found(self.scheme_of_work, self.scheme_of_work_id)

            data = Model.get_model(self.db, self.keyword_id, self.scheme_of_work_id, self.auth_user)
            self.model = data
            
            # if not found then raise error
            if self.keyword_id > 0:
                if self.model is None or self.model.is_from_db == False:
                    self.on_not_found(self.model, self.keyword_id)
                    
        except Http404 as e:
            raise e

        except Exception as e:
            self.error_message = repr(e)
            handle_log_exception(self.db, self.scheme_of_work_id, "An error occurred viewing keywords", e)
            # TODO: REMOVE swallow up and handle on form
            raise e


    def view(self):

        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "schemeofwork": self.scheme_of_work,
            "keyword": self.model,
            "schemeofwork_options": self.schemeofwork_options
        }

        return ViewModel(self.scheme_of_work.name, self.scheme_of_work.name, "Merge {} for {}".format(self.model.term, self.scheme_of_work.name), ctx=self.auth_user, data=data, active_model=self.model, error_message=self.error_message, alert_message=self.alert_message)
        