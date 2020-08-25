"""
View Models
"""
import io
from rest_framework import serializers, status
from shared.models.core.basemodel import try_int
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel

class SchemeOfWorkGetLatestViewModel(BaseViewModel):
    # TODO: #235 Rename to {ViewName}ViewModel
    def __init__(self, db, top, auth_user):
        self.model = []
        self.db = db

        try:
            # get model
            data = SchemeOfWorkModel.get_latest_schemes_of_work(self.db, top=5, auth_user=auth_user)
            self.model = data
        except Exception as e:
            self.error_message = repr(e)


    def view(self, main_heading, sub_heading):

        data = {
            "latest_schemes_of_work":self.model
        }
        
        return ViewModel("", main_heading, sub_heading, data=data, error_message=self.error_message)


class TopicGetOptionsListViewModel(BaseViewModel):
    #TODO: #235 Rename to {ViewName}ViewModel
    def __init__(self, db, topic_id, auth_user, lvl=2):
        self.model = TopicModel.get_options(db, topic_id=topic_id, auth_user=auth_user, lvl=lvl)


class KeywordGetOptionsListViewModel(BaseViewModel):
    # TODO: #235 Depracate not a matching View
    def __init__(self, db, auth_user):
        self.model = KeywordModel.get_options(db, auth_user)


class KeywordGetAllListViewModel(BaseViewModel):
    #TODO: #235 Depracate not a matching View
    def __init__(self, db, lesson_id):
        self.model = KeywordModel.get_all(db, lesson_id)


class KeywordGetModelViewModel(BaseViewModel):
    #TODO: #235 Depracate not a matching View
    def __init__(self, db, lesson_id, auth_user):
        self.db = db
        # get model

        data = KeywordModel.get_model(self.db, lesson_id, auth_user)

        self.model = data
        

class KeywordGetModelByTermsViewModel(BaseViewModel):

    def __init__(self, db, key_words_list, allow_all, auth_user):

        self.model = KeywordModel.get_by_terms(db, key_words_list, allow_all, auth_user)
        

class KeywordSaveViewModel(BaseViewModel):
    #TODO: Rename or Depracate. No matching View
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
                data = KeywordModel.save(self.db, self.model, published, auth_user)
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
