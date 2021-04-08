from django.urls import resolve, reverse
from django.test import TestCase
from api.notifications.views import NotificationListViewSet, NotificationDeleteViewSet

# Create your tests here.
class test_api_route_notification(TestCase):

    def test_url_resolves_to_NotificationListViewSet_view(self):
        url = resolve('/api/notifications/')
        self.assertEqual("api.notifications.index", url.url_name)
        self.assertEqual(type(url.func), type(NotificationListViewSet.as_view()))

        
    def test_url_resolves_to_NotificationListViewSet_view__reverse(self):
        url = reverse('api.notifications.index')
        self.assertEqual("/api/notifications/", url)


    def test_url_resolves_to_NotificationDeleteViewSet_view(self):
        url = resolve('/api/notifications/289288123/delete')
        self.assertEqual("api.notifications.delete", url.url_name)
        self.assertEqual(type(url.func), type(NotificationDeleteViewSet.as_view()))

        
    def test_url_resolves_to_NotificationDeleteViewSet_view__reverse(self):
        url = reverse('api.notifications.delete', args=[289288123])
        self.assertEqual("/api/notifications/289288123/delete", url)
