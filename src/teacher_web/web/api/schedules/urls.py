from django.urls import path

from .views import LessonScheduleViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('', LessonListViewSet.as_view(), name="api.lessons.get"),
    path('<str:class_code>', LessonScheduleViewSet.as_view(), name="api.schedule.get"),
]