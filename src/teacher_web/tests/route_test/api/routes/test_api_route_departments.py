from django.urls import resolve, reverse
from django.test import TestCase
from api.departments.views import DepartmentViewSet, DepartmentListViewSet
import web.urls

# Create your tests here.
class test_api_route_departments(TestCase):

    def test_url_resolves_to_DepartmentListViewSet_get(self):
        url = resolve('/api/institute/127671276711/department/')
        self.assertEqual("api.departments.getall", url.url_name)
        self.assertEqual(type(url.func), type(DepartmentListViewSet.as_view()))


    def test_url_resolves_to_DepartmentListViewSet_get__reverse(self):
        url = reverse("api.departments.getall", args=[127671276711])
        self.assertEqual("/api/institute/127671276711/department/", url)


    def test_url_resolves_to_DepartmentViewSet_get(self):
        url = resolve('/api/institute/127671276711/department/67')
        self.assertEqual("api.departments.get", url.url_name)
        self.assertEqual(type(url.func), type(DepartmentViewSet.as_view()))

    
    def test_url_resolves_to_DepartmentViewSet_get__reverse(self):
        url = reverse("api.departments.get", args=[127671276711, 67])
        self.assertEqual("/api/institute/127671276711/department/67", url)

