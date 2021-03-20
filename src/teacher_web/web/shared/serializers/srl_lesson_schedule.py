from rest_framework import serializers, status
from shared.models.cls_lesson_schedule import LessonScheduleModel
from .srl_keyword import KeywordModelSerializer

class LessonScheduleModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonScheduleModel
        fields = [
            "id",
            "lesson_id",
            "scheme_of_work_id",
            "department_id",
            "institute_id"
        ]
