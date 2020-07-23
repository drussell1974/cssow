from rest_framework import serializers, status
from shared.models.cls_lesson import LessonModel
from .srl_keyword import KeywordModelSerializer

class LessonModelSerializer(serializers.ModelSerializer):
    
    key_words = KeywordModelSerializer(many=True, read_only=True)

    class Meta:
        model = LessonModel
        fields = [
            "id", 
            "title", 
            "summary", 
            "order_of_delivery_id", 
            "scheme_of_work_id",
            "topic_id",
            "year_id",
            "key_stage_id",
            "published",
            "resources",
            "learning_objectives",
            "key_words",
            "number_of_resource"
        ]
