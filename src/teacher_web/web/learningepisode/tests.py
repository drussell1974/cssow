from django.urls import resolve
from django.test import TestCase
from learningepisode.views import index

# Create your tests here.
class LearningEpisodePageTest(TestCase):
    def test__lessons__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons')
        self.assertEqual(url.func, index)