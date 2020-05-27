from django.urls import resolve, reverse
from django.test import TestCase
from api.schemesofwork.views import SchemeOfWorkViewSet, SchemeOfWorkListViewSet
import web.urls

# Create your tests here.
class ApiSchemeOfWorkPageTest(TestCase):

    def test_url_resolves_to_SchemeOfWorkListViewSet_get(self):
        url = resolve('/api/schemesofwork/')
        self.assertEqual("api.schemesofwork.getall", url.url_name)
        self.assertEqual(type(url.func), type(SchemeOfWorkListViewSet.as_view()))


    def test_url_resolves_to_SchemeOfWorkListViewSet_get__reverse(self):
        url = reverse("api.schemesofwork.getall")
        self.assertEqual("/api/schemesofwork/", url)


    def test_url_resolves_to_SchemeOfWorkViewSet_get(self):
        url = resolve('/api/schemesofwork/127')
        self.assertEqual("api.schemesofwork.get", url.url_name)
        self.assertEqual(type(url.func), type(SchemeOfWorkViewSet.as_view()))

    
    def test_url_resolves_to_SchemeOfWorkViewSet_get__reverse(self):
        url = reverse("api.schemesofwork.get", args=[127])
        self.assertEqual("/api/schemesofwork/127", url)

