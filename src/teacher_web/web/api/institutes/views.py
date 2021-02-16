from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from .viewmodels import InstituteGetAllViewModel, InstituteGetModelViewModel

class InstituteViewSet(APIView):
    ''' API endpoint for a institute '''

    def get(self, request, institute_id):

        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=0)

        department_view = InstituteGetModelViewModel(db=db, institute_id=institute_id, auth_user=auth_ctx)
        return JsonResponse({"departments":department_view.model})


class InstituteListViewSet(APIView):
    ''' API endpoint for list of institutes '''

    def get (self, request):

        auth_ctx = AuthCtx(db, request, institute_id=0, department_id=0)

        #253 check user id
        departments_view = InstituteGetAllViewModel(db=db, auth_user=auth_ctx)
        return JsonResponse({"departments": departments_view.model})