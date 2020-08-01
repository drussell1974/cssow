from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse

# view models
from api.default.viewmodels import KeywordGetOptionsListViewModel, TopicGetOptionsListViewModel


class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request):

        keywords = KeywordGetOptionsListViewModel(db)
        
        return JsonResponse({"keywords": keywords.model }, safe = False)


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, topic_id):

        topics = TopicGetOptionsListViewModel(db, topic_id)

        return JsonResponse({"related-topics": topics.model}, safe = False)
    