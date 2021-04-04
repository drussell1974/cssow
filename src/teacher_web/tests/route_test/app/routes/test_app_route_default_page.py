from django.urls import resolve, reverse
from django.test import TestCase
from app.default.views import index, academic_year

# Create your tests here.
class test_app_route_default_page(TestCase):

    def test_root_url_resolves_to_index(self):
        url = resolve('/')
        self.assertEqual("default", url.url_name)
        self.assertEquals(url.func, index)

    
    def test_root_url_resolves_to_index__reverse(self):
        url = reverse("default")
        self.assertEqual("/", url)

        
    def test_change_academic_year__url_resolves_to_change_academic_year(self):
        url = resolve('/academic-year')
        self.assertEqual("default.academic-year", url.url_name)
        self.assertEquals(url.func, academic_year)

    
    def test_change_academic_year_url_resolves_to_change_academic_year__reverse(self):
        url = reverse("default.academic-year")
        self.assertEqual("/academic-year", url)
