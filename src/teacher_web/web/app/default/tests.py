from django.urls import resolve
from django.test import TestCase
from app.default.views import index

# Create your tests here.
class DefaultPageTest(TestCase):
    def test_root_url_resolves_to_index(self):
        url = resolve('/')
        self.assertEqual(url.func, index)