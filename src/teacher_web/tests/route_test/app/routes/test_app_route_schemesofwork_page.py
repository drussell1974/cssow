from django.urls import resolve, reverse
from django.test import TestCase
from app.schemesofwork.views import edit, index, delete_unpublished

# Create your tests here.
class test_app_route_schemesofwork_page(TestCase):

    def test__schemesofwork__url_resolves_to_index(self):
        url = resolve("/schemesofwork/")
        self.assertEqual("schemesofwork.index", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork__url_resolves_to_index__reverse(self):
        url = reverse("schemesofwork.index")
        self.assertEqual("/schemesofwork/", url)
    
    
    def test__schemeofwork_new__resolves_to_new(self):
        url = resolve("/schemesofwork/new")
        self.assertEqual("schemesofwork.new", url.url_name)
        self.assertEqual(url.func, edit)


    def test__schemeofwork_new__resolves_to_new__reverse(self):
        url = reverse("schemesofwork.new")
        self.assertEqual("/schemesofwork/new", url)


    def test__schemeofwork_view__resolves_to_view(self):
        url = resolve("/schemesofwork/127")
        self.assertEqual("schemesofwork.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemeofwork_view__resolves_to_view__reverse(self):
        url = reverse("schemesofwork.view", args=[127])
        self.assertEqual("/schemesofwork/127", url)


    def test__schemesofwork_edit__resolves_to_edit(self):
        url = resolve("/schemesofwork/127/edit")
        self.assertEqual("schemesofwork.edit", url.url_name)
        self.assertEqual(url.func, edit)


    def test__schemesofwork_edit__resolves_to_edit__reverse(self):
        url = reverse("schemesofwork.edit", args=[127])
        self.assertEqual("/schemesofwork/127/edit", url)


    def test__schemesofwork_publish_item__resolves_to_publish(self):
        url = resolve("/schemesofwork/127/publish")
        self.assertEqual("schemesofwork.publish_item", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_publish_item__resolves_to_publish__reverse(self):
        url = reverse("schemesofwork.publish_item", args=[127])
        self.assertEqual("/schemesofwork/127/publish", url)
