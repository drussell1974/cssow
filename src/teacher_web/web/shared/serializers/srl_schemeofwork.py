from shared.models.cls_schemeofwork import SchemeOfWorkModel
from rest_framework import serializers, status
from django.db import models

class SchemeOfWorkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemeOfWorkModel
        fields = ["id", "name", "description"]
