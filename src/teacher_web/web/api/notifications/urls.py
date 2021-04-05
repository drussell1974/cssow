from django.urls import path

from .views import NotificationListViewSet

urlpatterns = [
    path("", NotificationListViewSet.as_view(), name="api.notifications.index")
]