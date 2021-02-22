from shared.models.cls_institute import InstituteModel
from rest_framework import serializers, status
from django.db import models

class InstituteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteModel
        fields = ["id", "name", "description", "number_of_departments"]
