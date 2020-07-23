"""
View Models
"""
import io
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from shared.models.cls_topic import TopicModel, get_options
from shared.models.cls_keyword import KeywordDataAccess, KeywordModel
from shared.serializers.srl_keyword import KeywordModelSerializer
from shared.serializers.srl_topic import TopicModelSerializer


class TopicGetOptionsListViewModel():
    data = []

    def __init__(self, db, topic_id, lvl=2):
        rows = get_options(db, topic_id=topic_id, lvl=lvl)

        for topic in rows:
            
            srlz = TopicModelSerializer(topic)

            self.data.append(srlz.data)


class KeywordGetOptionsListViewModel:
    data = []

    def __init__(self, db):
        
        self.data = []

        rows = KeywordDataAccess.get_options(db)

        for keyword in rows:
            srl = KeywordModelSerializer(keyword)
            self.data.append(srl.data)


class KeywordGetAllListViewModel:
    list = []
    #json = []

    def __init__(self, db, lesson_id):
        rows = KeywordDataAccess.get_all(db, lesson_id)

        for keyword in rows:
            srl = KeywordModelSerializer(keyword)
            self.list.append(srl.data)


class KeywordGetModelViewModel:
    model = None
    json = {}

    def __init__(self, db, lesson_id, auth_user):
        self.db = db
        # get model
        data = KeywordDataAccess.get_model(self.db, lesson_id, auth_user)
        self.model = data
        # serialize model to json
        srl = KeywordModelSerializer(data)
        self.json = srl.data


class KeywordGetModelByTermsViewModel:
    model = None
    json = None

    def __init__(self, db, key_words_list, allow_all, auth_user):

        data = KeywordDataAccess.get_by_terms(db, key_words_list, allow_all, auth_user)
        self.model = data
        srl = KeywordModelSerializer(self.model)
        self.json = srl.data


class KeywordSaveViewModel:
    model = {}
    #json = {}

    def __init__(self, db):
        self.db = db

    def from_model(self, model):
        self.model = KeywordModel
        # TODO: serialise to json

    #def from_json(self, json):
    #    stream = io.BytesIO(json)
    #    data = JSONParser().parse(stream)
    #    m = KeywordModel().from_json(data)


    def execute(self, auth_user, published=1):
        # TODO: validate
        data = KeywordDataAccess.save(self.db, self.model)
        self.model = data
