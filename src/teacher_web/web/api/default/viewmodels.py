
import io
from rest_framework import serializers, status
from rest_framework.parsers import JSONParser
from shared.models.cls_topic import TopicModel, get_options
from shared.models.cls_keyword import KeywordDataAccess, KeywordModel
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.serializers.srl_keyword import KeywordModelSerializer
from shared.serializers.srl_topic import TopicModelSerializer


class TopicGetOptionsListViewModel(BaseViewModel):

    def __init__(self, db, topic_id, lvl=2):
        data = get_options(db, topic_id=topic_id, lvl=lvl)
        self.model = list(map(lambda m: TopicModelSerializer(m).data,data))


class KeywordGetOptionsListViewModel(BaseViewModel):

    def __init__(self, db):

        data = KeywordDataAccess.get_options(db)

        self.model = list(map(lambda m: KeywordModelSerializer(m).data, data))
