from django.urls import resolve
from django.test import TestCase
from schemesofwork.views import index

# Create your tests here.
class SchemesOfWorkPageTest(TestCase):
    def test_root_url_resolves_to_index(self):
        url = resolve('/schemesofwork/')
        self.assertEqual(url.func, index)