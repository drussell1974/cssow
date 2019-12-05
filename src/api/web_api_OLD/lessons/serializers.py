from schemeofwork.modules.cls_learningepisode import LearningEpisodeModel
from rest_framework import serializers

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = LearningEpisodeModel(id_=0, title="")
        fields = ["title", "summary"]

    