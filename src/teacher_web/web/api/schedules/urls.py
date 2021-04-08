from django.urls import path

from .views import LessonScheduleClassCodeViewSet, LessonScheduleViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('', LessonListViewSet.as_view(), name="api.lessons.get"),
    path('lesson/<str:class_code>', LessonScheduleClassCodeViewSet.as_view(), name="api.schedule.classcode"),
    path('institute/<int:institute_id>/department/<int:department_id>/schemesofwork/<int:scheme_of_work_id>/lessons/<int:lesson_id>/events', LessonScheduleViewSet.as_view(), name="api.schedule.get"),
]