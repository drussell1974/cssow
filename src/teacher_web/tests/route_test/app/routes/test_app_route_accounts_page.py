from django.urls import resolve, reverse
from django.test import TestCase
from app.accounts.views import index, RegisterUserView

# Create your tests here.
class test_app_route_accounts_page(TestCase):

    def test_index_url_resolves_to_account(self):
        url = resolve('/accounts/')
        self.assertEqual("accounts.index", url.url_name)
        self.assertEquals(url.func, index)


    def test_index_url_resolves_to_account__reverse(self):
        url = reverse("accounts.index")
        self.assertEqual("/accounts/", url)


    def test_register_url_resolves_to_register(self):
        url = resolve('/accounts/register/')
        self.assertEqual("accounts.register", url.url_name)
        self.assertEquals(url.func.__name__, RegisterUserView.as_view().__name__)

    
    def test_register_url_resolves_to_register__reverse(self):
        url = reverse("accounts.register")
        self.assertEqual("/accounts/register/", url)

        