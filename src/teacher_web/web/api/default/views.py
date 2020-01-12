from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from cssow.models import cls_keyword, cls_topic


class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request):
        key_words = cls_keyword.get_options(db)
        return JsonResponse({"keywords": key_words})


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, topic_id):
        topics = cls_topic.get_options(db, topic_id=topic_id, lvl=2)
        return JsonResponse({"related-topics": topics})
    