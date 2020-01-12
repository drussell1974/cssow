from django.urls import resolve
from django.test import TestCase
from app.learningobjectives.views import index

# Create your tests here.
class LearningObjectivesPageTest(TestCase):
    def test__learningobjective_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/')
        self.assertEqual("learningobjective.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__learningobjective_delete_item__url_resolves_to_delete(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/1/delete')
        self.assertEqual("learningobjective.delete_item", url.url_name)
        self.assertEqual(url.func, index)
        
    
    def test__learningobjective_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/1/edit')
        self.assertEqual("learningobjective.edit", url.url_name)
        self.assertEqual(url.func, index)