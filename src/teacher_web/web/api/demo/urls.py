from django.urls import path

from .views import RestoreDemoDataApiView

urlpatterns = [
    path('restore-data', RestoreDemoDataApiView.as_view(), name="api.demo.restore-data"),
    path('', RestoreDemoDataApiView.as_view(), name="api.demo.index"),
]