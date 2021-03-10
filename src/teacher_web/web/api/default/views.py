from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from api.default.viewmodels import KeywordGetOptionsListViewModel, TopicGetOptionsListViewModel


class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request, institute_id, department_id, scheme_of_work_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        keywords = KeywordGetOptionsListViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        
        return JsonResponse({"keywords": keywords.model }, safe = False)


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, institute_id, department_id, topic_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, topic_id=topic_id)

        topics_view = TopicGetOptionsListViewModel(db=db, topic_id=topic_id, auth_user=auth_ctx)

        return JsonResponse({"related-topics": topics_view.model}, safe = False)
    