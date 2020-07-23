from shared.models.cls_resource import ResourceModel
from rest_framework import serializers, status
from django.db import models

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceModel
        fields = ["id", "title"]