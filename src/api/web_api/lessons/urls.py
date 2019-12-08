from django.urls import path

from .views import LessonViewSet, LessonListViewSet


app_name = "schemeofwork"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('schemeofwork/<int:scheme_of_work_id>/lessons', LessonListViewSet.as_view(), name="lessons"),
    path('schemeofwork/<int:scheme_of_work_id>/lessons/<int:lesson_id>', LessonViewSet.as_view()),
]