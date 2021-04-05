from shared.models.cls_eventlog import EventLogModel
from rest_framework import serializers, status
from django.db import models

class EventLogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLogModel
        fields = ["id", "message", "action"]
