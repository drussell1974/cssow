import json
from django.http import Http404
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from app.default.viewmodels import KeywordGetModelByTermsViewModel, KeywordSaveViewModel, KeywordGetAllListViewModel


class LessonIndexViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.model = []
        self.db = db
        self.scheme_of_work_id = scheme_of_work_id
        self.scheme_of_work_name = SchemeOfWorkModel.get_schemeofwork_name_only(db, scheme_of_work_id)
        # name to appear
        if self.scheme_of_work_name is None or self.scheme_of_work_name == "":
            self.on_not_found(self.scheme_of_work_name, scheme_of_work_id)
        # side menu options
        self.schemeofwork_options = SchemeOfWorkModel.get_options(db, auth_user=auth_user)
        # get list of lessons
        data = Model.get_all(self.db, scheme_of_work_id, auth_user)
        self.model = data
        

    def view(self):

        data = {
            "scheme_of_work_id":self.scheme_of_work_id,
            "schemeofwork_options": self.schemeofwork_options,
            "lessons": self.model,
            "topic_name": "",
        }

        return ViewModel(self.scheme_of_work_name, self.scheme_of_work_name, "Lessons", data=data)


class LessonGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        model = Model.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)

        #248 Http404
        if lesson_id > 0:
            if model is None or model.is_from_db == False:
                self.on_not_found(model, lesson_id, scheme_of_work_id)

        self.model = model


class LessonEditViewModel(BaseViewModel):

    def __init__(self, db, data, key_words_json, auth_user):

        self.db = db
        self.auth_user = auth_user

        # assign data directly to the model

        self.model = data

        try:
            
            # transform key_words from string to dictionary list
            decoded_key_words = list(map(lambda item: KeywordModel().from_dict(item), json.loads(key_words_json)))
                    
            #handle_log_warning(self.db, "processing key words", decoded_key_words)

            # TODO: move to execute function for saving
            for keyword in decoded_key_words:
                
                # get or insert
                save_keyword = KeywordSaveViewModel(db, keyword)
                
                kyw_model = save_keyword.execute(auth_user)

                
                self.model.key_words.append(kyw_model)
    
        except Exception as ex:
            handle_log_exception(db, "An error occurred processing key words json", ex)
            raise


    def execute(self, published):
        self.model.validate()

        if self.model.is_valid == True:
            data = Model.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            #    raise Exception("Lesson is not valid! {}".format(self.model.validation_errors))
            handle_log_warning(self.db, "saving lesson", "lesson is not valid (id:{}, title:{}, validation_errors (count:{}).".format(self.model.id, self.model.title, len(self.model.validation_errors)))

        return self.model


class LessonPublishViewModel(BaseViewModel):

    def __init__(self, db, auth_user, lesson_id):
        self.model = Model.publish(db, auth_user, lesson_id)
    

class LessonDeleteViewModel(BaseViewModel):

    def __init__(self, db, auth_user, lesson_id):
        self.model = Model.delete(db, auth_user, lesson_id)


class LessonDeleteUnpublishedViewModel(BaseViewModel):
    
    def __init__(self, db, auth_user, lesson_id):
        self.model = Model.delete_unpublished(db, auth_user, lesson_id)
