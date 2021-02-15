from django.urls import resolve, reverse
from django.test import TestCase
from api.schemesofwork.views import SchemeOfWorkViewSet, SchemeOfWorkListViewSet
import web.urls

# Create your tests here.
class test_api_route_schemeofwork(TestCase):

    def test_url_resolves_to_SchemeOfWorkListViewSet_get(self):
        url = resolve('/api/institute/127671276711/department/67/schemesofwork/')
        self.assertEqual("api.schemesofwork.getall", url.url_name)
        self.assertEqual(type(url.func), type(SchemeOfWorkListViewSet.as_view()))


    def test_url_resolves_to_SchemeOfWorkListViewSet_get__reverse(self):
        url = reverse("api.schemesofwork.getall", args=[127671276711, 67])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/", url)


    def test_url_resolves_to_SchemeOfWorkViewSet_get(self):
        url = resolve('/api/institute/127671276711/department/67/schemesofwork/127')
        self.assertEqual("api.schemesofwork.get", url.url_name)
        self.assertEqual(type(url.func), type(SchemeOfWorkViewSet.as_view()))

    
    def test_url_resolves_to_SchemeOfWorkViewSet_get__reverse(self):
        url = reverse("api.schemesofwork.get", args=[127671276711, 67, 127])
        self.assertEqual("/api/institute/127671276711/department/67/schemesofwork/127", url)

