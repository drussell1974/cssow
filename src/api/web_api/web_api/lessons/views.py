from rest_framework import viewsets
from modules.schemeofwork.learningepisode import LearningEpisodeModel, get_all

class LessonViewSet(viewsets.ModelViewSet):
    ''' API endpoint for lessons '''
    queryset = get_all(None, 0, None)
    serializer_class = LearningEpisodeModel