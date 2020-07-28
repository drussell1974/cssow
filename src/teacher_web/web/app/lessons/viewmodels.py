import json
from rest_framework import serializers, status
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from app.default.viewmodels import KeywordGetModelViewModel, KeywordGetModelByTermsViewModel, KeywordSaveViewModel, KeywordGetAllListViewModel
from shared.serializers.srl_keyword import KeywordModelSerializer

class LessonGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        self.model = []

        self.db = db
        # get model
        data = LessonDataAccess.get_all(self.db, scheme_of_work_id, auth_user)
        self.model = data


class LessonGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, auth_user, resource_type_id = 0):
        self.db = db
        # get model
        data = LessonDataAccess.get_model(self.db, lesson_id, auth_user, resource_type_id)
        self.model = data


class LessonSaveViewModel(BaseViewModel):

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
            data = LessonDataAccess.save(self.db, self.model, self.auth_user, published)
            self.model = data   
        else:
            #    raise Exception("Lesson is not valid! {}".format(self.model.validation_errors))
            handle_log_warning(self.db, "saving lesson", "lesson is not valid (id:{}, title:{}, validation_errors (count:{}).".format(self.model.id, self.model.title, len(self.model.validation_errors)))

        return self.model

