from django.urls import path

from .views import SchemeOfWorkViewSet, SchemeOfWorkListViewSet


app_name = "schemesofwork"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('<int:scheme_of_work_id>', SchemeOfWorkViewSet.as_view(), name="api.schemesofwork.get"),
    path('', SchemeOfWorkListViewSet.as_view(), name="api.schemesofwork.getall"),
]