
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

