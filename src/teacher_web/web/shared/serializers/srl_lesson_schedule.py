from rest_framework import serializers, status
from shared.models.cls_lesson_schedule import LessonScheduleModel
from .srl_keyword import KeywordModelSerializer

class LessonScheduleModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LessonScheduleModel
        fields = [
            "id",
            "title",
            "class_name",
            "start_date",
            "class_code",
            "lesson_id",
            "scheme_of_work_id",
            "department_id",
            "institute_id",
            "is_from_db",
            "whiteboard_url",
        ]
