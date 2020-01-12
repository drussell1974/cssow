from django.urls import resolve
from django.test import TestCase
from app.schemesofwork.views import index

# Create your tests here.
class SchemesOfWorkPageTest(TestCase):

    def test__schemesofwork__url_resolves_to_index(self):
        url = resolve('/schemesofwork/')
        self.assertEqual("schemesofwork.index", url.url_name)
        self.assertEqual(url.func, index)
    
    
    def test__schemeofwork_new__resolves_to_new(self):
        url = resolve('/schemesofwork/new')
        self.assertEqual("schemesofwork.new", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemeofwork_view__resolves_to_view(self):
        url = resolve('/schemesofwork/127')
        self.assertEqual("schemesofwork.view", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_edit__resolves_to_edit(self):
        url = resolve('/schemesofwork/127/edit')
        self.assertEqual("schemesofwork.edit", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_delete__resolves_to_delete(self):
        url = resolve('/schemesofwork/127/delete')
        self.assertEqual("schemesofwork.delete_item", url.url_name)
        self.assertEqual(url.func, index)


    def test__schemesofwork_delete__resolves_to_publish(self):
        url = resolve('/schemesofwork/127/publish')
        self.assertEqual("schemesofwork.publish_item", url.url_name)
        self.assertEqual(url.func, index)
