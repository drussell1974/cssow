from django.urls import path

from .views import DepartmentViewSet, DepartmentListViewSet

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('<int:department_id>', DepartmentViewSet.as_view(), name="api.departments.get"),
    path('', DepartmentListViewSet.as_view(), name="api.departments.getall"),
]