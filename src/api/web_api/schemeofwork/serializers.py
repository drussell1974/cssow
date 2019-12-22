from models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkListModel
from rest_framework import serializers, status
from django.db import models

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeOfWorkModel
        fields = ["id", "name", "description"]


class SchemeOfWorkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeOfWorkListModel
        fields = ["schemeofwork"]