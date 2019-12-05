#from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from schemeofwork.learningepisode import get_all, get_model
from .serializers import LessonSerializer, LessonListSerializer


@csrf_exempt
def get_lesson(request, scheme_of_work_id, lesson_id):
    """
    List specific lessons.
    """
    lesson = get_model(None, lesson_id, None)
    serializer = LessonSerializer(lesson)

    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_all_lessons(request, scheme_of_work_id):
    """
    List all lessons.
    """
    lessons = get_all(None, scheme_of_work_id, None)  
    serializer = LessonListSerializer(lessons, many=True)

    return JsonResponse(serializer.data, safe=False)

"""
class LessonViewSet(viewsets.ModelViewSet):
    ''' API endpoint for a lesson '''
    queryset = []
    serializer_class = LessonSerializer

    
class LessonListViewSet(viewsets.ModelViewSet):
    ''' API endpoint for list of lessons '''
    queryset = []
    serializer_class = LessonListSerializer
    """