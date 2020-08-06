from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .viewmodels import ResourceGetModelViewModel

class ResourceViewSet(APIView):
    ''' API endpoint for a lesson '''

    def get(self, request, scheme_of_work_id, lesson_id, resource_id):

        resource_view = ResourceGetModelViewModel(db, resource_id, scheme_of_work_id, request.user.id)

        return JsonResponse({"resource": resource_view.model})
