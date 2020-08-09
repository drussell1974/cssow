from django.urls import path

from .views import ResourceViewSet, ResourceMarkdownViewSet
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('<int:resource_id>', ResourceViewSet.as_view(), name="api.resource.get"),
    path('<int:resource_id>/markdown/<str:md_document_name>', ResourceMarkdownViewSet.as_view(), name="api.resource.markdown")
]