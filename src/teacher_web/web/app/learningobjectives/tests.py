from django.urls import resolve, reverse
from django.test import TestCase
from app.learningobjectives.views import index

# Create your tests here.
class LearningObjectivesPageTest(TestCase):
    def test__learningobjective_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/')
        self.assertEqual("learningobjective.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__learningobjective_index__url_resolves_to_index__reverse(self):
        url = reverse("learningobjective.index", args=[127, 32])
        self.assertEqual("/schemesofwork/127/lessons/32/learningobjectives/", url)

    
    def test__learningobjective_delete_item__url_resolves_to_delete(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/1/delete')
        self.assertEqual("learningobjective.delete_item", url.url_name)
        self.assertEqual(url.func, index)
        

    def test__learningobjective_delete_item__url_resolves_to_delete__reverse(self):
        url = reverse("learningobjective.delete_item", args=[127, 32, 1])
        self.assertEqual("/schemesofwork/127/lessons/32/learningobjectives/1/delete", url)
    

    def test__learningobjective_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/32/learningobjectives/1/edit')
        self.assertEqual("learningobjective.edit", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__learningobjective_edit__url_resolves_to_edit__reverse(self):
        url = reverse("learningobjective.edit", args=[127, 32, 1])
        self.assertEqual("/schemesofwork/127/lessons/32/learningobjectives/1/edit", url)