from django.urls import resolve, reverse
from django.test import TestCase
from api.schedules.views import LessonScheduleViewSet, LessonScheduleClassCodeViewSet

# Create your tests here.
class test_api_route_schedule(TestCase):

    def test_url_resolves_to_LessonClassCodeViewSet_get(self):
        url = resolve("/api/schedule/lesson/ABCDEF")
        self.assertEqual("api.schedule.classcode", url.url_name)
        self.assertEqual(type(url.func), type(LessonScheduleClassCodeViewSet.as_view()))

    
    def test_url_resolves_to_LessonClassCodeViewSet_get__reverse(self):
        url = reverse('api.schedule.classcode', args=["ABCDEF"])
        self.assertEqual("/api/schedule/lesson/ABCDEF", url)


    def test_url_resolves_to_LessonScheduleViewSet_get(self):
        url = resolve('/api/schedule/institute/2/department/5/schemesofwork/11/lessons/220/events')
        self.assertEqual("api.schedule.get", url.url_name)
        self.assertEqual(type(url.func), type(LessonScheduleViewSet.as_view()))

    
    def test_url_resolves_to_LessonScheduleViewSet_get__reverse(self):
        url = reverse("api.schedule.get", args=[2,5,11,220])
        self.assertEqual("/api/schedule/institute/2/department/5/schemesofwork/11/lessons/220/events", url)