from django.urls import path

from .views import NotificationListViewSet, NotificationDeleteViewSet

urlpatterns = [
    path("", NotificationListViewSet.as_view(), name="api.notifications.index"),
    path("<int:id>/delete", NotificationDeleteViewSet.as_view(), name="api.notifications.delete")
]