from django.urls import resolve, reverse
from django.test import TestCase
from app.lesson_keywords.views import index, select, new, edit, delete_item, save, publish_item, delete_unpublished

# Create your tests here.
class test_app_route_lesson_keywords_page(TestCase):


    def test__keywords_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/lessons/32/keywords/')
        self.assertEqual("lesson_keywords.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__keywords_index__url_resolves_to_index__reverse(self):
        url = reverse("lesson_keywords.index", args=[127, 32])
        self.assertEqual("/schemesofwork/127/lessons/32/keywords/", url)

    
    def test__keywords_delete_item__url_resolves_to_delete(self):
        url = resolve('/schemesofwork/127/lessons/32/keywords/1/delete')
        self.assertEqual("lesson_keywords.delete_item", url.url_name)
        self.assertEqual(url.func, delete_item)
        

    def test__keywords_delete_item__url_resolves_to_delete__reverse(self):
        url = reverse("lesson_keywords.delete_item", args=[127, 32, 1])
        self.assertEqual("/schemesofwork/127/lessons/32/keywords/1/delete", url)
    

    def test__keywords_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/lessons/32/keywords/1/edit')
        self.assertEqual("lesson_keywords.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__keywords_edit__url_resolves_to_edit__reverse(self):
        url = reverse("lesson_keywords.edit", args=[127, 32, 1])
        self.assertEqual("/schemesofwork/127/lessons/32/keywords/1/edit", url)


    def test__keywords_select__url_resolves_to_select(self):
        url = resolve('/schemesofwork/127/lessons/32/keywords/select')
        self.assertEqual("lesson_keywords.select", url.url_name)
        self.assertEqual(url.func, select)

    
    def test__keywords_select__url_resolves_to_select__reverse(self):
        url = reverse("lesson_keywords.select", args=[127, 32])
        self.assertEqual("/schemesofwork/127/lessons/32/keywords/select", url)
    

    def test__keywords_save__url_resolves_to_save(self):    
        url = resolve('/schemesofwork/127/lessons/32/keywords/99/save')
        self.assertEqual("lesson_keywords.save", url.url_name)
        self.assertEqual(url.func, save)

    
    def test__keywords_save__url_resolves_to_save__reverse(self):
        url = reverse("lesson_keywords.save", args=[127, 32, 99])
        self.assertEqual("/schemesofwork/127/lessons/32/keywords/99/save", url)


    def test__keywords_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve("/schemesofwork/11/lessons/32/keywords/delete_unpublished")
        self.assertEqual("lesson_keywords.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)
        
    
    def test__keywords_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("lesson_keywords.delete_unpublished", args=[11, 32])
        self.assertEqual("/schemesofwork/11/lessons/32/keywords/delete_unpublished", url)