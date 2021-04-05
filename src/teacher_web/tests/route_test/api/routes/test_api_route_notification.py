from django.urls import resolve, reverse
from django.test import TestCase
from api.notifications.views import NotificationListViewSet

# Create your tests here.
class test_api_route_notification(TestCase):

    def test_url_resolves_to_NotificationListViewSet_view(self):
        url = resolve('/api/notifications/')
        self.assertEqual("api.notifications.index", url.url_name)
        self.assertEqual(type(url.func), type(NotificationListViewSet.as_view()))

        
    def test_url_resolves_to_NotificationListViewSet_view__reverse(self):
        url = reverse('api.notifications.index')
        self.assertEqual("/api/notifications/", url)