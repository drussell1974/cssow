from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import Ctx
from shared.models.core.django_helper import auth_user_model
from .viewmodels import SchemeOfWorkGetAllViewModel, SchemeOfWorkGetModelViewModel

class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''

    def get(self, request, scheme_of_work_id):

        view_ctx = Ctx(scheme_of_work_id=scheme_of_work_id)

        # TODO: #329 move to view model
        auth_ctx = auth_user_model(db, request, ctx=view_ctx)

        #253 check user id
        schemeofwork_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        return JsonResponse({"schemeofwork":schemeofwork_view.model})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request):

        view_ctx = Ctx()

        # TODO: #329 move to view model
        auth_ctx = auth_user_model(db, request, ctx=view_ctx)

        #253 check user id
        schemesofwork_view = SchemeOfWorkGetAllViewModel(db=db, auth_user=auth_user_model(db, request, ctx=auth_ctx))
        return JsonResponse({"schemesofwork": schemesofwork_view.model})