from django.urls import resolve, reverse
from django.test import TestCase
from app.accounts.views import index, delete, RegisterTeacherView, JoinAsTeacherView

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
        self.assertEquals(url.func.__name__, RegisterTeacherView.as_view().__name__)

    
    def test_register_url_resolves_to_register__reverse(self):
        url = reverse("accounts.register")
        self.assertEqual("/accounts/register/", url)
        

    def test_join_url_resolves_to_join(self):
        url = resolve('/accounts/join/')
        self.assertEqual("accounts.join", url.url_name)
        self.assertEquals(url.func.__name__, JoinAsTeacherView.as_view().__name__)

    
    def test_join_url_resolves_to_join__reverse(self):
        url = reverse("accounts.join")
        self.assertEqual("/accounts/join/", url)


    def test_delete_url_resolves_to_delete(self):
        url = resolve('/accounts/delete/')
        self.assertEqual("accounts.delete", url.url_name)
        self.assertEquals(url.func, delete)

    
    def test_delete_url_resolves_to_delete__reverse(self):
        url = reverse("accounts.delete")
        self.assertEqual("/accounts/delete/", url)
        