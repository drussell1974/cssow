from django.urls import path

from .views import SchemeOfWorkViewSet, SchemeOfWorkListViewSet


app_name = "schemeofwork"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('schemeofwork', SchemeOfWorkListViewSet.as_view(), name="schemesofwork"),
    path('schemeofwork/<int:scheme_of_work_id>', SchemeOfWorkViewSet.as_view(), name="schemeofwork"),
]