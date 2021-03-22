from django.urls import resolve, reverse
from django.test import TestCase
from api.schedules.views import LessonScheduleViewSet

# Create your tests here.
class test_api_route_schedule(TestCase):

    def test_url_resolves_to_LessonClassCode_get(self):
        url = resolve("/api/schedule/lesson/ABCDEF")
        self.assertEqual("api.schedule.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonScheduleViewSet.as_view()))

    
    def test_url_resolves_to_LessonClassCodet_get__reverse(self):
        url = reverse('api.schedule.get', args=["ABCDEF"])
        self.assertEqual("/api/schedule/lesson/ABCDEF", url)

