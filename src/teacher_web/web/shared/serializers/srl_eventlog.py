from shared.models.cls_notification import NotifyModel
from rest_framework import serializers, status
from django.db import models

class NotifyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifyModel
        fields = ["id", "notify_message", "action"]
