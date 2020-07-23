import json as to_json
from rest_framework import serializers, status
from shared.models.core.log import handle_log_info
from shared.models.core.basemodel import try_int
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from app.default.viewmodels import KeywordGetModelViewModel, KeywordGetModelByTermsViewModel, KeywordSaveViewModel, KeywordGetAllListViewModel


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
        if self.model is not None:
            # get each terms for each item 
            key_word_map = map(lambda m: m.term, self.model.key_words)
            # assign as comma seperated list
            self.model.key_words_str = ",".join(list(key_word_map))


class LessonSaveViewModel(BaseViewModel):

    def __init__(self, db, data, auth_user):
        
        self.db = db
        self.auth_user = auth_user

        if type(data) is Model:
            key_word_ids = data.key_words 

            # assign data directly to the model
            self.model = data

            # transform key_words
            self.model.key_words = []
        
        
            for keyword_id in key_word_ids.split(","):
                # get or insert
                save_keyword = KeywordSaveViewModel(db, keyword_id)
                save_keyword.execute(auth_user)
                self.model.key_words.append(save_keyword.model)


    def execute(self, published=1):
        data = LessonDataAccess.save(self.db, self.model, self.auth_user, published)
        self.model = data        
