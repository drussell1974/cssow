from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from shared.models.core.context import AuthCtx, Ctx
from .viewmodels import LessonScheduleClassCodeViewModel, LessonScheduleViewModel

class LessonScheduleClassCodeViewSet(APIView):
    ''' API endpoint for a lesson schedule '''

    def get(self, request, class_code, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        #institute_id = request.GET.get("institute_id")
        auth_ctx = Ctx(0, 0)
        
        #class_code = request.GET.get("class_code", "")

        #253 check user id
        get_schedule_view = LessonScheduleClassCodeViewModel(db=db, class_code=class_code, auth_ctx=auth_ctx)

        return JsonResponse({ "schedule": get_schedule_view.model } )
    

class LessonScheduleViewSet(APIView):
    ''' API endpoint for events '''

    def resolve_url(self, schedule):
        whiteboard_url = reverse("lesson_schedule.whiteboard_view", args=[schedule.institute_id, schedule.department_id, schedule.scheme_of_work_id, schedule.lesson_id, schedule.id])
        edit_url = reverse("lesson_schedule.edit", args=[schedule.institute_id, schedule.department_id, schedule.scheme_of_work_id, schedule.lesson_id, schedule.id])
        return {
            "lesson_schedule.whiteboard_view":whiteboard_url, 
            "lesson_schedule.edit":edit_url
        }


    def get(self, request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id)
        
        #class_code = request.GET.get("class_code", "")

        #253 check user id
        get_schedule_view = LessonScheduleViewModel(db=db, scheme_of_work_id=scheme_of_work_id, lesson_id=lesson_id, auth_ctx=auth_ctx, fn_resolve_url=self.resolve_url)

        return JsonResponse({ "schedule": get_schedule_view.model } )
    