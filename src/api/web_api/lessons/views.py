from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models.cls_learningepisode import get_model, get_all
from .serializers import LessonSerializer, LessonListSerializer


class LessonViewSet(APIView):
    ''' API endpoint for a lesson '''
    #serializer_class = LessonSerializer

    def get(self, request, scheme_of_work_id, lesson_id):
        lesson = get_model(None, lesson_id, None).__dict__
        return Response({"lesson":lesson})
    
    
class LessonListViewSet(APIView):
    ''' API endpoint for list of lessons '''
    #queryset =  get_all(None, 11, None)
    #serializer_class = LessonListSerializer

    def get (self, request, scheme_of_work_id):
        lessons = get_all(None, scheme_of_work_id, None)
        return Response({"lessons": lessons})