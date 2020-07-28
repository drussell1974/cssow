"""
View Models
"""
import io
from rest_framework import serializers, status
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.cls_topic import TopicModel, get_options
from shared.models.cls_keyword import KeywordDataAccess, KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel


class TopicGetOptionsListViewModel(BaseViewModel):
    def __init__(self, db, topic_id, lvl=2):
        self.model = get_options(db, topic_id=topic_id, lvl=lvl)


class KeywordGetOptionsListViewModel(BaseViewModel):

    def __init__(self, db):
        self.model = KeywordDataAccess.get_options(db)


class KeywordGetAllListViewModel(BaseViewModel):

    def __init__(self, db, lesson_id):
        self.model = KeywordDataAccess.get_all(db, lesson_id)


class KeywordGetModelViewModel(BaseViewModel):
    
    def __init__(self, db, lesson_id, auth_user):
        self.db = db
        # get model

        data = KeywordDataAccess.get_model(self.db, lesson_id, auth_user)

        self.model = data
        

class KeywordGetModelByTermsViewModel(BaseViewModel):

    def __init__(self, db, key_words_list, allow_all, auth_user):

        self.model = KeywordDataAccess.get_by_terms(db, key_words_list, allow_all, auth_user)
        

class KeywordSaveViewModel(BaseViewModel):

    def __init__(self, db, model):
        self.db = db
        self.model = model


    def execute(self, auth_user, published=1):

        if type(self.model) is KeywordModel:
        
            if self.model.id == 0:
                """ check the term does already existing create instanace """
                model_found = self._find_by_term(self.db, self.model.term,  auth_user)

                if model_found is not None:
                    handle_log_warning(self.db, "saving keyword", "keyword already exists. Using existing item. (keyword id:{}, term:'{}', definition:'{}')".format(self.model.id, self.model.term, self.model.definition))
                    # assign found model
                    self.model = model_found

            self.model.validate()

            if self.model.is_valid == True:
                data = KeywordDataAccess.save(self.db, self.model)
                self.model = data
            else:
                handle_log_warning(self.db, "saving keyword", "keywordnot valid (keyword id:{}, term:'{}', definition:'{}')".format(self.model.id, self.model.term, self.model.definition))
        else:
            raise AttributeError("Cannot save KeywordModel of type {}".format(type(self.model)))
        
        return self.model


    def _find_keyword_by_id(self, db, id, auth_user):
        """ Get the model by id """
        
        get_keyword = KeywordGetModelViewModel(db, id, auth_user)

        return get_keyword.model


    def _find_by_term(self, db, term, auth_user):
        """ search by term """

        get_keyword = KeywordGetModelByTermsViewModel(db, term, allow_all=True, auth_user=auth_user)
        
        if get_keyword.model is None or len(get_keyword.model) == 0:
            return None
        else:
            return get_keyword.model[0]


    def _find_or_create_by_term(self, db, term, definition, auth_user):
        """ search by term and create new if necessary"""

        get_keyword = KeywordGetModelByTermsViewModel(db, term, allow_all=True, auth_user=auth_user)
        
        if get_keyword.model is None or len(get_keyword.model) == 0:
            return KeywordModel(0, term, definition)
        else:
            return get_keyword.model[0]
