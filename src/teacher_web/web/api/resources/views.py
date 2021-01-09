from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.models.core.django_helper import auth_user_id
from .viewmodels import ResourceGetModelViewModel, ResourceGetMarkdownViewModel

class ResourceViewSet(APIView):
    ''' API endpoint for a resource '''

    def get(self, request, scheme_of_work_id, lesson_id, resource_id):

        #253 check user id
        resource_view = ResourceGetModelViewModel(db=db, resource_id=resource_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))

        return JsonResponse({"resource": resource_view.model})


class ResourceMarkdownViewSet(APIView):
    ''' API endpoint for a markdown of a resource of type MARKDOWN '''
    
    def get(self, request, scheme_of_work_id, lesson_id, resource_id, md_document_name):
        
        #253 check user id
        markdown_view = ResourceGetMarkdownViewModel(MARKDOWN_STORAGE=settings.MARKDOWN_STORAGE, resource_id=resource_id, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, md_document_name=md_document_name, auth_user=auth_user_id(request))

        return JsonResponse({"markdown": markdown_view.model})