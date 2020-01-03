from django.urls import resolve
from django.test import TestCase
from schemesofwork.views import index

# Create your tests here.
class SchemesOfWorkPageTest(TestCase):

    def test__schemesofwork__url_resolves_to_index(self):
        url = resolve('/schemesofwork/')
        self.assertEqual(url.func, index)
    
    
    def test__schemeofwork_new__resolves_to_new(self):
        url = resolve('/schemesofwork/new')
        self.skipTest("not implemented")
        self.assertEqual(url.func, index)


    def test__schemeofwork_view__resolves_to_view(self):
        url = resolve('/schemesofwork/127')
        self.skipTest("not implemented")
        self.assertEqual(url.func, index)


    def test__schemesofwork_edit__resolves_to_edit(self):
        url = resolve('/schemesofwork/127/edit')
        self.skipTest("not implemented")
        self.assertEqual(url.func, index)

        
    def test__schemesofwork_delete__resolves_to_delete(self):
        url = resolve('/schemesofwork/127/delete')
        self.skipTest("not implemented")
        self.assertEqual(url.func, index)


    def test__schemesofwork_delete__resolves_to_delete(self):
        url = resolve('/schemesofwork/127/publish')
        self.skipTest("not implemented")
        self.assertEqual(url.func, index)
