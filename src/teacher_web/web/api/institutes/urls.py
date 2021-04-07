from django.urls import path

from .views import InstituteViewSet, InstituteListViewSet, InstituteScheduleViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('<int:institute_id>', InstituteViewSet.as_view(), name="api.institutes.get"),
    path('<int:institute_id>/schedule', InstituteScheduleViewSet.as_view(), name="api.institutes.schedule"),
    path('', InstituteListViewSet.as_view(), name="api.institutes.getall"),
]