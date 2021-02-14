from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import Ctx
from shared.models.core.django_helper import auth_user_model

# view models
from api.default.viewmodels import KeywordGetOptionsListViewModel, TopicGetOptionsListViewModel


class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request, scheme_of_work_id):

        view_ctx = Ctx(scheme_of_work_id=scheme_of_work_id)

        # TODO: #329 move to view model
        auth_ctx = auth_user_model(db, request, ctx=view_ctx)

        keywords = KeywordGetOptionsListViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        
        return JsonResponse({"keywords": keywords.model }, safe = False)


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, topic_id):

        view_ctx = Ctx(topic_id=topic_id)

        # TODO: #329 move to view model
        auth_ctx = auth_user_model(db, request, ctx=view_ctx)

        topics_view = TopicGetOptionsListViewModel(db=db, topic_id=topic_id, auth_user=auth_ctx)

        return JsonResponse({"related-topics": topics_view.model}, safe = False)
    