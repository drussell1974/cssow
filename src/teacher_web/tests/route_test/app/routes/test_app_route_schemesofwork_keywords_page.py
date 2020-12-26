from django.urls import resolve, reverse
from django.test import TestCase
from app.keywords.views import index, new, edit, delete_item, save, publish_item, delete_unpublished

# Create your tests here.
class test_app_route_schemesofwork_keywords_page(TestCase):


    def test__keywords_index__url_resolves_to_index(self):
        url = resolve('/schemesofwork/127/keywords/')
        self.assertEqual("keywords.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__keywords_index__url_resolves_to_index__reverse(self):
        url = reverse("keywords.index", args=[127])
        self.assertEqual("/schemesofwork/127/keywords/", url)

    
    def test__keywords_delete_item__url_resolves_to_delete(self):
        url = resolve('/schemesofwork/127/keywords/1/delete')
        self.assertEqual("keywords.delete_item", url.url_name)
        self.assertEqual(url.func, delete_item)
        

    def test__keywords_delete_item__url_resolves_to_delete__reverse(self):
        url = reverse("keywords.delete_item", args=[127, 1])
        self.assertEqual("/schemesofwork/127/keywords/1/delete", url)
    

    def test__keywords_edit__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/keywords/1/edit')
        self.assertEqual("keywords.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__keywords_edit__url_resolves_to_edit__reverse(self):
        url = reverse("keywords.edit", args=[127, 1])
        self.assertEqual("/schemesofwork/127/keywords/1/edit", url)


    def test__keywords_new__url_resolves_to_edit(self):
        url = resolve('/schemesofwork/127/keywords/new')
        self.assertEqual("keywords.new", url.url_name)
        self.assertEqual(url.func, new)

    
    def test__keywords_new__url_resolves_to_edit__reverse(self):
        url = reverse("keywords.new", args=[127])
        self.assertEqual("/schemesofwork/127/keywords/new", url)
    

    def test__keywords_save__url_resolves_to_save(self):    
        url = resolve('/schemesofwork/127/keywords/99/save')
        self.assertEqual("keywords.save", url.url_name)
        self.assertEqual(url.func, save)

    
    def test__keywords_save__url_resolves_to_save__reverse(self):
        url = reverse("keywords.save", args=[127, 99])
        self.assertEqual("/schemesofwork/127/keywords/99/save", url)


    def test__keywords_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve("/schemesofwork/11/keywords/delete_unpublished")
        self.assertEqual("keywords.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)
        
    
    def test__keywords_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("keywords.delete_unpublished", args=[11])
        self.assertEqual("/schemesofwork/11/keywords/delete_unpublished", url)