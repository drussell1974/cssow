from django.urls import resolve, reverse
from django.test import TestCase
from app.schemesofwork.views import edit, index, delete_unpublished

# Create your tests here.
class test_app_route_schemesofwork_page(TestCase):

    def test__schemesofwork__url_resolves_to_index(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/")
        self.assertEqual("schemesofwork.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork__url_resolves_to_index__reverse(self):
        url = reverse("schemesofwork.index",  args=[12711761271176,1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/", url)
    
    
    def test__schemeofwork_new__resolves_to_new(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/new")
        self.assertEqual("schemesofwork.new", url.url_name)
        self.assertEqual(url.func, edit)


    def test__schemeofwork_new__resolves_to_new__reverse(self):
        url = reverse("schemesofwork.new",  args=[12711761271176,1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/new", url)


    def test__schemeofwork_view__resolves_to_view(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127")
        self.assertEqual("schemesofwork.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemeofwork_view__resolves_to_view__reverse(self):
        url = reverse("schemesofwork.view",  args=[12711761271176,1271176,127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127", url)


    def test__schemesofwork_edit__resolves_to_edit(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/edit")
        self.assertEqual("schemesofwork.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__schemesofwork_edit__resolves_to_edit__reverse(self):
        url = reverse("schemesofwork.edit",  args=[12711761271176,1271176,127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/edit", url)


    def test__schemesofwork_delete_unpublished__resolves_to_delete_unpublished(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/delete_unpublished")
        self.assertEqual("schemesofwork.delete_unpublished", url.url_name)
        self.assertEqual(url.func, delete_unpublished)


    def test__schemesofwork_delete_unpublished__resolves_to_delete_unpublished__reverse(self):
        url = reverse("schemesofwork.delete_unpublished", args=[12711761271176,1271176])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/delete_unpublished", url)


    def test__schemesofwork_publish_item__resolves_to_publish(self):
        url = resolve("/institute/12711761271176/department/1271176/schemesofwork/127/publish")
        self.assertEqual("schemesofwork.publish_item", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_publish_item__resolves_to_publish__reverse(self):
        url = reverse("schemesofwork.publish_item", args=[12711761271176,1271176,127])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/127/publish", url)
