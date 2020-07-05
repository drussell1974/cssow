from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.models import cls_ks123pathway, cls_lesson, cls_learningobjective

from .serializers import LessonSerializer, LessonListSerializer


class LessonViewSet(APIView):
    ''' API endpoint for a lesson '''

    def get(self, request, scheme_of_work_id, lesson_id):
        
        resource_type_id = request.GET.get("resource_type_id", 0)

        lesson = cls_lesson.get_model(db, lesson_id, request.user.id, resource_type_id)
        return JsonResponse({"lesson": lesson})
    
    
class LessonListViewSet(APIView):
    ''' API endpoint for list of lessons '''
    
    def get (self, request, scheme_of_work_id):
        lessons = cls_lesson.get_all(db, scheme_of_work_id, request.user.id)
        return JsonResponse({"lessons": lessons})


class LessonPathwayObjectivesViewSet(APIView):
    ''' API endpoint for list of lessons pathway objectives'''

    def get(self, request, scheme_of_work_id, lesson_id, key_stage_id, key_words = None):
        ''' get the pathway objectives '''
        pathwayobjectives = cls_learningobjective.get_all_pathway_objectives(db, key_stage_id = key_stage_id, key_words = key_words)
        should_be_checked = cls_lesson.get_pathway_objective_ids(db, lesson_id)

        return JsonResponse({
            "pathway-objectives": pathwayobjectives, 
            "should-be-checked": should_be_checked 
        })

    '''
    def _view_pathway_objectives_readonly(request, scheme_of_work_id, lesson_id):
        #lesson_id = 0 if request.vars.lesson_id  is None else request.vars.lesson_id

        data = cls_learningobjective.get_linked_pathway_objectives(db, lesson_id = lesson_id)

        return dict(data=data)
    '''


class LessonPathwayKs123ViewSet(APIView):
    def get(self, request, scheme_of_work_id, lesson_id, year_id, topic_id):
        '''
        lesson_id = 0 if request.vars.lesson_id  is None else request.vars.lesson_id
        year_id = 0 if request.vars.year_id is None else request.vars.year_id
        topic_id = 0 if request.vars.topic_id is None else request.vars.topic_id
        '''
        data = cls_ks123pathway.get_options(db, year_id = year_id, topic_id = topic_id)
        should_be_checked = cls_ks123pathway.get_linked_pathway_ks123(db, lesson_id)

        ks123pathway = []
        for item in data:
            for check in should_be_checked:
                if item.id == check[0]:
                    item.is_checked = True
                else:
                    item.is_checked = False

            ks123pathway.append(item)

        #return dict(view_model=view_model)
        return JsonResponse({"ks123-pathway": ks123pathway})

    '''
    def _view_pathway_ks123_readonly(request, scheme_of_work_id, lesson_id):
        #lesson_id = 0 if request.vars.lesson_id  is None else request.vars.lesson_id

        data = cls_ks123pathway.get_linked_pathway_ks123(db, lesson_id = lesson_id)

        return dict(data=data)
    '''