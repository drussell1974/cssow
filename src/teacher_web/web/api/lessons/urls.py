from django.urls import path

from .views import LessonViewSet, LessonListViewSet, LessonPathwayObjectivesViewSet, LessonPathwayKs123ViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('', LessonListViewSet.as_view(), name="api.lessons.get"),
    path('<int:lesson_id>', LessonViewSet.as_view(), name="api.lesson.get"),
    path('<int:lesson_id>/pathway-ks123/year/<int:year_id>/topic/<int:topic_id>', LessonPathwayKs123ViewSet.as_view(), name="api.lesson.pathway-ks123"),
    #<int:learning_objective_id>/pathway-objectives/key-stage/<int:key_stage_id>/keywords/<str:key_words>
    path('<int:lesson_id>/pathway-objectives/key-stage/<int:key_stage_id>/keywords/<str:key_words>', LessonPathwayObjectivesViewSet.as_view(), name='api.lesson.pathway-objectives'),
    path('<int:lesson_id>/pathway-objectives/key-stage/<int:key_stage_id>/keywords/', LessonPathwayObjectivesViewSet.as_view(), name='api.lesson.pathway-objectives'),
]