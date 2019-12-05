from rest_framework import viewsets
from schemeofwork.learningepisode import LearningEpisodeModel, LearningEpisodeListModel, get_all

def lessons():
    pass

class LessonViewSet(viewsets.ModelViewSet):
    ''' API endpoint for lessons '''
    queryset = get_all(None, 0, None)
    serializer_class = LearningEpisodeModel

    
class LessonListViewSet(viewsets.ModelViewSet):
    ''' API endpoint for lessons '''
    def get_queryset(self):
        return get_all(None, 0, None)
    #serializer_class = LearningEpisodeListModel