from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from .viewmodels import DepartmentGetAllViewModel, DepartmentGetModelViewModel

class DepartmentViewSet(APIView):
    ''' API endpoint for a department '''

    def get(self, request, institute_id, department_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id)

        department_view = DepartmentGetModelViewModel(db=db, department_id=department_id, auth_user=auth_ctx)
        return JsonResponse({"department":department_view.model})


class DepartmentListViewSet(APIView):
    ''' API endpoint for list of departments '''

    def get (self, request, institute_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=0)

        #253 check user id
        departments_view = DepartmentGetAllViewModel(db=db, institute_id=institute_id, auth_user=auth_ctx)
        return JsonResponse({"departments": departments_view.model})