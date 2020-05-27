from rest_framework.views import APIView
#from rest_framework.parsers import JSONParser
#from rest_framework.response import Response
#from django.forms.models import model_to_dict
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from models.cls_schemeofwork import get_model, get_all
#from .serializers import SchemeOfWorkListViewSet


class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''
    #serializer_class = LessonSerializer

    def get(self, request, scheme_of_work_id):
        schemeofwork = get_model(None, scheme_of_work_id, None).__dict__
        return JsonResponse({"schemeofwork":schemeofwork})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''
    #queryset =  get_all(None, 11, None)
    #serializer_class = LessonListSerializer

    def get (self, request):
        schemesofwork = get_all(None, 0, None)
        return JsonResponse({"schemesofwork": schemesofwork})