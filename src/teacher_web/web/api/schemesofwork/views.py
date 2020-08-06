from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from .viewmodels import SchemeOfWorkGetAllViewModel, SchemeOfWorkGetModelViewModel

class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''

    def get(self, request, scheme_of_work_id):
        schemeofwork_view = SchemeOfWorkGetModelViewModel(db, scheme_of_work_id, request.user.id)
        return JsonResponse({"schemeofwork":schemeofwork_view.model})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request):
        schemesofwork_view = SchemeOfWorkGetAllViewModel(db, request.user.id)
        return JsonResponse({"schemesofwork": schemesofwork_view.model})