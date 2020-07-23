from rest_framework import serializers, status
from shared.models.cls_topic import TopicModel, get_options

class TopicModelSerializer(serializers.ModelSerializer):
   
    id = 0
    name = ""

    class Meta:
        model = TopicModel
        fields = ["id", "name"]
