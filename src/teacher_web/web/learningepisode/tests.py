from django.urls import resolve
from django.test import TestCase
from learningepisode.views import index

# Create your tests here.
class LessonsPageTest(TestCase):
    def test_root_url_resolves_to_index(self):
        url = resolve('/lessons/1')
        self.assertEqual(url.func, index)