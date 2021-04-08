from django.urls import path

from .views import InstituteViewSet, InstituteListViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('<int:institute_id>', InstituteViewSet.as_view(), name="api.institutes.get"),
    path('', InstituteListViewSet.as_view(), name="api.institutes.getall"),
]