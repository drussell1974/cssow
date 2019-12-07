from schemeofwork.cls_learningepisode import LearningEpisodeModel, LearningEpisodeListModel
from rest_framework import serializers, status
from django.db import models

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningEpisodeModel
        fields = ["id", "title"]


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningEpisodeListModel
        fields = ["lessons"]