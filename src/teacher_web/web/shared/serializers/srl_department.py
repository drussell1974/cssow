from shared.models.cls_department import DepartmentModel
from rest_framework import serializers, status
from django.db import models

class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = ["id", "name", "description", "number_of_schemes_of_work"]
