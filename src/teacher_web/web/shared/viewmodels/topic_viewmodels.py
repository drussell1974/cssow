from rest_framework import serializers, status
from django.db import models
from shared.models.cls_topic import TopicModel, get_options


class TopicModelSerializer(serializers.ModelSerializer):
   
    id = 0
    name = ""

    class Meta:
        model = TopicModel
        fields = ["id", "name"]


class TopicGetOptionsListViewModel():
    data = []

    def __init__(self, db, topic_id, lvl=2):
        rows = get_options(db, topic_id=topic_id, lvl=lvl)

        for topic in rows:
            
            srlz = TopicModelSerializer(topic)

            self.data.append(srlz.data)