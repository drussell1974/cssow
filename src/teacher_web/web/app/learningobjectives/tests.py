from django.urls import resolve
from django.test import TestCase
from learningobjectives.views import index

# Create your tests here.
class LearningObjectivesPageTest(TestCase):
    def test__learningobjective_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives')
        self.assertEqual(url.func, index)