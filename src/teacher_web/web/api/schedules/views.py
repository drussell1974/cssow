from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.models.core.context import Ctx
from .viewmodels import LessonScheduleViewModel

class LessonScheduleViewSet(APIView):
    ''' API endpoint for a lesson schedule '''

    def get(self, request, class_code, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        #institute_id = request.GET.get("institute_id")
        auth_ctx = Ctx(0, 0)
        
        #class_code = request.GET.get("class_code", "")

        #253 check user id
        get_schedule_view = LessonScheduleViewModel(db=db, class_code=class_code, auth_ctx=auth_ctx)

        return JsonResponse({ "schedule": get_schedule_view.model } )
    