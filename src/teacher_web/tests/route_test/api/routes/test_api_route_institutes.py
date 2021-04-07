from django.urls import resolve, reverse
from django.test import TestCase
from api.institutes.views import InstituteViewSet, InstituteListViewSet, InstituteScheduleViewSet
import web.urls

# Create your tests here.
class test_api_route_institutes(TestCase):

    def test_url_resolves_to_InstituteListViewSet_get(self):
        url = resolve('/api/institute/')
        self.assertEqual("api.institutes.getall", url.url_name)
        self.assertEqual(type(url.func), type(InstituteListViewSet.as_view()))


    def test_url_resolves_to_InstituteListViewSet_get__reverse(self):
        url = reverse("api.institutes.getall")
        self.assertEqual("/api/institute/", url)


    def test_url_resolves_to_InstituteViewSet_get(self):
        url = resolve('/api/institute/127671276711')
        self.assertEqual("api.institutes.get", url.url_name)
        self.assertEqual(type(url.func), type(InstituteViewSet.as_view()))

    
    def test_url_resolves_to_InstituteViewSet_get__reverse(self):
        url = reverse("api.institutes.get", args=[127671276711])
        self.assertEqual("/api/institute/127671276711", url)


    def test_url_resolves_to_InstituteScheduleViewSet_get(self):
        url = resolve('/api/institute/127671276711/schedule')
        self.assertEqual("api.institutes.schedule", url.url_name)
        self.assertEqual(type(url.func), type(InstituteScheduleViewSet.as_view()))

    
    def test_url_resolves_to_InstituteScheduleViewSet_get__reverse(self):
        url = reverse("api.institutes.schedule", args=[127671276711])
        self.assertEqual("/api/institute/127671276711/schedule", url)

