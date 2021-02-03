from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.django_helper import auth_user_id
from .viewmodels import SchemeOfWorkGetAllViewModel, SchemeOfWorkGetModelViewModel

class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''

    def get(self, request, scheme_of_work_id):
        #253 check user id
        schemeofwork_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
        return JsonResponse({"schemeofwork":schemeofwork_view.model})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request):
        #253 check user id
        schemesofwork_view = SchemeOfWorkGetAllViewModel(db=db, auth_user=auth_user_id(request))
        return JsonResponse({"schemesofwork": schemesofwork_view.model})