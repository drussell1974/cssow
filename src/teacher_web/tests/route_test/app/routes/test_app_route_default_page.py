from django.urls import resolve, reverse
from django.test import TestCase
from app.default.views import index

# Create your tests here.
class test_app_route_default_page(TestCase):

    def test_root_url_resolves_to_index(self):
        url = resolve('/')
        self.assertEqual("default", url.url_name)
        self.assertEquals(url.func, index)

    
    def test_root_url_resolves_to_index__reverse(self):
        url = reverse("default")
        self.assertEqual("/", url)



        