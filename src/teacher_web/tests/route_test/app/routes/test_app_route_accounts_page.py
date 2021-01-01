from django.urls import resolve, reverse
from django.test import TestCase
from app.default.views import profile

# Create your tests here.
class test_app_route_accounts_page(TestCase):

    def test_root_url_resolves_to_index(self):
        url = resolve('/accounts/profile/')
        self.assertEqual("profile", url.url_name)
        self.assertEquals(url.func, profile)

    
    def test_root_url_resolves_to_index__reverse(self):
        url = reverse("profile")
        self.assertEqual("/accounts/profile/", url)



        