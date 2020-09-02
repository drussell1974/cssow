from rest_framework import serializers, status
from shared.models.cls_keyword import KeywordModel as Model

class KeywordModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ["id", "term", "definition", "scheme_of_work_id"]
