from django.urls import resolve, reverse
from django.test import TestCase
from app.department.views import edit, viewall, index, delete_unpublished

# Create your tests here.
class test_app_route_department_page(TestCase):

    def test__department__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/")
        self.assertEqual("department.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__department__url_resolves_to_index__reverse(self):
        url = reverse("department.index", args=[12711761271176])
        self.assertEqual("/institute/12711761271176/department/", url)
    
    
    def test__department__url_resolves_to_all(self):
        url = resolve("/institute/12711761271176/department/all")
        self.assertEqual("department.all", url.url_name)
        self.assertEqual(url.func, viewall)


    def test__department__url_resolves_to_all__reverse(self):
        url = reverse("department.all", args=[12711761271176])
        self.assertEqual("/institute/12711761271176/department/all", url)
    
    
    def test__department_new__resolves_to_new(self):
        url = resolve("/institute/12711761271176/department/new")
        self.assertEqual("department.new", url.url_name)
        self.assertEqual(url.func, edit)


    def test__department_new__resolves_to_new__reverse(self):
        url = reverse("department.new", args=[12711761271176])
        self.assertEqual("/institute/12711761271176/department/new", url)


    def test__department_view__resolves_to_view(self):
        url = resolve("/institute/12711761271176/department/1271176")
        self.assertEqual("department.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__department_view__resolves_to_view__reverse(self):
        url = reverse("department.view", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176", url)


    def test__department_edit__resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/edit")
        self.assertEqual("department.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__department_edit__resolves_to_edit__reverse(self):
        url = reverse("department.edit", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/edit", url)


    def test__department_delete_unpublished__resolves_to_delete_unpublished(self):
        url = resolve("/institute/12711761271176/department/delete_unpublished")
        self.assertEqual("department.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)


    def test__department_delete_unpublished__resolves_to_delete_unpublished__reverse(self):
        url = reverse("department.delete_unpublished", args=[12711761271176])
        self.assertEqual("/institute/12711761271176/department/delete_unpublished", url)

'''
    def test__department_publish_item__resolves_to_publish(self):
        url = resolve("/institute/12711761271176/department/1271176/publish")
        self.assertEqual("department.publish_item", url.url_name)
        self.assertEqual(url.func, index)


    def test__department_publish_item__resolves_to_publish__reverse(self):
        url = reverse("department.publish_item", args=[12711761271176, 1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/publish", url)
        '''
