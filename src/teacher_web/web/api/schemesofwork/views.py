from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.cls_schemeofwork import SchemeOfWorkDataAccess


class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''

    def get(self, request, scheme_of_work_id):
        schemeofwork = SchemeOfWorkDataAccess.get_model(db, scheme_of_work_id, request.user.id).__dict__
        return JsonResponse({"schemeofwork":schemeofwork})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request):
        schemesofwork = SchemeOfWorkDataAccess.get_all(db, 0, request.user.id)
        return JsonResponse({"schemesofwork": schemesofwork})