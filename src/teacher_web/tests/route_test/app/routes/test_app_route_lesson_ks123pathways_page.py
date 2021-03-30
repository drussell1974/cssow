from django.urls import resolve, reverse
from django.test import TestCase
from app.lesson_ks123pathways.views import select #, index, new, edit, delete_item, save, publish_item, delete_unpublished

# Create your tests here.
class test_app_route_lesson_ks123pathways_page(TestCase):

    ### TODO: create index - for now go to select
    
    def test__pathways_index__url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/')
        self.assertEqual("lesson_ks123pathways.index", url.url_name)
        self.assertEqual(url.func, select) #index)

    
    def test__pathways_index__url_resolves_to_index__reverse(self):
        url = reverse("lesson_ks123pathways.index", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/", url)
    
    """    
    def test__pathways_delete_item__url_resolves_to_delete(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/1/delete')
        self.assertEqual("lesson_ks123pathways.delete_item", url.url_name)
        self.assertEqual(url.func, delete_item)
        

    def test__pathways_delete_item__url_resolves_to_delete__reverse(self):
        url = reverse("lesson_ks123pathways.delete_item", args=[12711761271176, 1271176, 127, 32, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/1/delete", url)
    

    def test__pathways_edit__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/1/edit')
        self.assertEqual("lesson_ks123pathways.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__pathways_edit__url_resolves_to_edit__reverse(self):
        url = reverse("lesson_ks123pathways.edit", args=[12711761271176, 1271176, 127, 32, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/1/edit", url)
    """

    def test__pathways_select__url_resolves_to_select(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/select')
        self.assertEqual("lesson_ks123pathways.select", url.url_name)
        self.assertEqual(url.func, select)

    
    def test__pathways_select__url_resolves_to_select__reverse(self):
        url = reverse("lesson_ks123pathways.select", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/select", url)
    
    """
    def test__pathways_save__url_resolves_to_save(self):    
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/99/save')
        self.assertEqual("lesson_ks123pathways.save", url.url_name)
        self.assertEqual(url.func, save)

    
    def test__pathways_save__url_resolves_to_save__reverse(self):
        url = reverse("lesson_ks123pathways.save", args=[12711761271176, 1271176, 127, 32, 99])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/pathways/99/save", url)


    def test__pathways_delete_unpublished__url_resolves_to_delete_unpublished(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/32/pathways/delete_unpublished")
        self.assertEqual("lesson_ks123pathways.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)
        
    
    def test__pathways_delete_unpublished__url_resolves_to_delete_unpublished__reverse(self):
        url = reverse("lesson_ks123pathways.delete_unpublished", args=[12711761271176, 1271176, 11, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/11/lessons/32/pathways/delete_unpublished", url)
    """