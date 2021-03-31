from django.urls import resolve, reverse
from django.test import TestCase
from app.ks123pathways.views import index, edit, delete_unpublished, save 

# Create your tests here.
class test_app_route_ks123pathways_page(TestCase):

    def test__pathways_index__url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/pathways/')
        self.assertEqual("ks123pathways.index", url.url_name)
        self.assertEqual(url.func, index) #index)

    
    def test__pathways_index__url_resolves_to_index__reverse(self):
        url = reverse("ks123pathways.index", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/pathways/", url)
    

    def test__pathways_edit__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/pathways/1/edit')
        self.assertEqual("ks123pathways.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__pathways_edit__url_resolves_to_edit__reverse(self):
        url = reverse("ks123pathways.edit", args=[12711761271176, 1271176, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/pathways/1/edit", url)
    

    def test__pathways_new__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/pathways/new')
        self.assertEqual("ks123pathways.new", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__pathways_new__url_resolves_to_edit__reverse(self):
        url = reverse("ks123pathways.new", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/pathways/new", url)
    

    def test__pathways_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve("/institute/12711761271176/department/1271176/pathways/delete_unpublished")
        self.assertEqual("ks123pathways.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)
        
    
    def test__pathways_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("ks123pathways.delete_unpublished", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/pathways/delete_unpublished", url)
