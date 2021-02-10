from django.urls import resolve, reverse
from django.test import TestCase
from app.resources.views import index, new, edit, delete_item, save, delete_unpublished, publish_item

# Create your tests here.
class test_app_route_resources_page(TestCase):
    
    def test__resources_index__url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/')
        self.assertEqual("resource.index", url.url_name)
        self.assertEqual(url.func, index)

    
    def test__resources_index__url_resolves_to_index__reverse(self):
        url = reverse("resource.index", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/", url)

    
    def test__resources_delete_item__url_resolves_to_delete(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/1/delete')
        self.assertEqual("resource.delete_item", url.url_name)
        self.assertEqual(url.func, delete_item)
        

    def test__resources_delete_item__url_resolves_to_delete__reverse(self):
        url = reverse("resource.delete_item", args=[12711761271176, 1271176, 127, 32, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/1/delete", url)
    

    def test__resources_edit__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/1/edit')
        self.assertEqual("resource.edit", url.url_name)
        self.assertEqual(url.func, edit)

    
    def test__resources_edit__url_resolves_to_edit__reverse(self):
        url = reverse("resource.edit", args=[12711761271176, 1271176, 127, 32, 1])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/1/edit", url)


    def test__resources_new__url_resolves_to_edit(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/new')
        self.assertEqual("resource.new", url.url_name)
        self.assertEqual(url.func, new)

    
    def test__resources_new__url_resolves_to_edit__reverse(self):
        url = reverse("resource.new", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/new", url)
    

    def test__resources_save__url_resolves_to_save(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/99/save')
        self.assertEqual("resource.save", url.url_name)
        self.assertEqual(url.func, save)

    
    def test__resources_save__url_resolves_to_save__reverse(self):
        url = reverse("resource.save", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/99/save", url)


    def test__resources_delete_unpublished__url_resolves_to_save(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/delete_unpublished')
        self.assertEqual("resource.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)

    
    def test__resources_save__url_resolves_to_save__reverse(self):
        url = reverse("resource.delete_unpublished", args=[12711761271176, 1271176, 127, 32])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/32/resources/delete_unpublished", url)


    def test__learningobjective_publish__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/resources/545/publish_item")
        self.assertEqual("resource.publish_item", url.url_name)
        self.assertEqual(url.func, publish_item)


    def test__learningobjective_publish__url_resolves_to_index__reverse(self):
        url = reverse("resource.publish_item", args=[12711761271176, 1271176, 127,13,545])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/lessons/13/resources/545/publish_item", url)


