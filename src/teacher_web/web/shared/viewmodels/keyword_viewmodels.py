"""
View Models
"""
import io
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel as Model

class KeywordModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ["id", "term", "definition"]


class KeywordGetAllListViewModel:
    keywords = []
    def __init__(self, db, search_term):
        
        # TODO: remove __dict__ . The object should be serialised to json further up the stack
        #self.__dict__keywords.append(Model.get_all(db, search_term))
        pass


class KeywordGetOptionsListViewModel:
    data = []

    def __init__(self, db):
        
        self.data = []

        rows = DataAccess.get_options(db)

        for keyword in rows:
            srl = KeywordModelSerializer(keyword)
            self.data.append(srl.data)


class KeywordGetModelViewModel:
    model = None
    json = {}

    def __init__(self, db, lesson_id, auth_user):
        self.db = db
        # get model
        data = DataAccess.get_model(self.db, lesson_id, auth_user)
        self.model = data
        # serialize model to json
        srl = KeywordModelSerializer(data)
        self.json = srl.data


class KeywordGetModelByTermsViewModel:
    model = None
    json = None

    def __init__(self, db, key_words_list, allow_all, auth_user):

        data = DataAccess.get_by_terms(db, key_words_list, allow_all, auth_user)
        self.model = data
        srl = KeywordModelSerializer(self.model)
        self.json = srl.data


class KeywordSaveViewModel:
    model = {}
    #json = {}

    def __init__(self, db):
        self.db = db

    def from_model(self, model):
        self.model = Model
        # TODO: serialise to json

    #def from_json(self, json):
    #    stream = io.BytesIO(json)
    #    data = JSONParser().parse(stream)
    #    m = KeywordModel().from_json(data)


    def execute(self, auth_user, published=1):
        # TODO: validate
        data = DataAccess.save(self.db, self.model)
        self.model = data