from shared.models.cls_lesson import LessonModel, LessonListModel
from rest_framework import serializers, status
from django.db import models

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = ["id", "title"]


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonListModel
        fields = ["lessons"]