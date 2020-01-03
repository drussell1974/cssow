from django.urls import resolve
from django.test import TestCase
from app.learningepisode.views import index, new

# Create your tests here.
class LearningEpisodePageTest(TestCase):
    def test__learningepisode_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/')
        self.assertEqual(url.func, index)

    def test__learningepisode_new__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/new')
        self.assertEqual(url.func, new)