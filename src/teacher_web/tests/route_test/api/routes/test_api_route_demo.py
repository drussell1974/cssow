from django.urls import resolve, reverse
from django.test import TestCase
from api.demo.views import RestoreDemoDataApiView

# Create your tests here.
class test_api_route_demo(TestCase):

    def test_url_resolves_to_RestoreTestDataApiView_view(self):
        url = resolve('/api/demo/restore-data')
        self.assertEqual("api.demo.restore-data", url.url_name)
        self.assertEqual(type(url.func), type(RestoreDemoDataApiView.as_view()))


    def demo_url_resolves_to_RestoreTestDataApiView__reverse(self):
        url = reverse("api.demo.restore-data", args=[1,2])
        self.assertEqual("/api/demo/restore-data", url)
