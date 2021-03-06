from django.urls import resolve, reverse
from django.test import TestCase
from api.default.views import RestoreTestDataApiView

# Create your tests here.
class test_api_route_restore_test_data(TestCase):

    def test_url_resolves_to_RestoreTestDataApiView_view(self):
        url = resolve('/api/institute/1/department/2/restore-test-data')
        self.assertEqual("api.default.restore-test-data", url.url_name)
        self.assertEqual(type(url.func), type(RestoreTestDataApiView.as_view()))


    def test_url_resolves_to_RestoreTestDataApiView__reverse(self):
        url = reverse("api.default.restore-test-data", args=[1,2])
        self.assertEqual("/api/institute/1/department/2/restore-test-data", url)
