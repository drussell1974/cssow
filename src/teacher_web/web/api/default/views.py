from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse

from shared.models.core.django_helper import auth_user_id

# view models
from api.default.viewmodels import KeywordGetOptionsListViewModel, TopicGetOptionsListViewModel


class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request, scheme_of_work_id):

        keywords = KeywordGetOptionsListViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
         
        return JsonResponse({"keywords": keywords.model }, safe = False)


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, topic_id):

        topics_view = TopicGetOptionsListViewModel(db=db, topic_id=topic_id, auth_user=auth_user_id(request))

        return JsonResponse({"related-topics": topics_view.model}, safe = False)
    