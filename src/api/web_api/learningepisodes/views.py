from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models.cls_lesson import get_model, get_all
from .serializers import lessonsSerializer, lessonsListSerializer


class LessonsViewSet(APIView):
    ''' API endpoint for a lesson '''

    def get(self, request, scheme_of_work_id, lesson_id):
        lesson = get_model(None, lesson_id, None)
        return JsonResponse({"lesson": lesson})
    
    
class LessonsListViewSet(APIView):
    ''' API endpoint for list of lesson '''
    
    def get (self, request, scheme_of_work_id):
        lessons = get_all(None, scheme_of_work_id, None)
        return JsonResponse({"lessons": lessons})