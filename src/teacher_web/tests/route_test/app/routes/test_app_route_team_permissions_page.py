from django.urls import resolve, reverse
from django.test import TestCase
from app.teampermissions.views import index, edit, delete, request_access, TeamPermissionRequestLoginView

# Create your tests here.
class test_app_route_team_permissions_page(TestCase):

    def test_index_url_resolves_to_account_team_permissions(self):
        url = resolve('/accounts/team-permissions/')
        self.assertEqual("team-permissions.index", url.url_name)
        self.assertEquals(url.func, index)


    def test_index_url_resolves_to_account_team_permissions__reverse(self):
        url = reverse("team-permissions.index")
        self.assertEqual("/accounts/team-permissions/", url)


    def test_edit_url_resolves_to_account__team_permissions_edit(self):
        url = resolve('/accounts/team-permissions/schemeofwork/56/teacher/6069/edit')
        self.assertEqual("team-permissions.edit", url.url_name)
        self.assertEquals(url.func, edit)

    
    def test_edit_url_resolves_to_account_team_permissions_edit__reverse(self):
        url = reverse("team-permissions.edit", args=[56,6069])
        self.assertEqual("/accounts/team-permissions/schemeofwork/56/teacher/6069/edit", url)


    def test_delete_url_resolves_to_account__team_permissions_delete(self):
        url = resolve('/accounts/team-permissions/schemeofwork/56/teacher/6069/delete')
        self.assertEqual("team-permissions.delete", url.url_name)
        self.assertEquals(url.func, delete)

    
    def test_delete_url_resolves_to_account_team_permissions_delete__reverse(self):
        url = reverse("team-permissions.delete", args=[56, 6069])
        self.assertEqual("/accounts/team-permissions/schemeofwork/56/teacher/6069/delete", url)


    def test_requestaccess_url_resolves_to_account__team_permissions_requestaccess(self):
        url = resolve('/accounts/team-permissions/schemeofwork/56/teacher/SCHEMEOFWORK.VIEWER/request-access')
        self.assertEqual("team-permissions.request-access", url.url_name)
        self.assertEquals(url.func, request_access)

    
    def test_requestaccess_url_resolves_to_account_team_permissions_requestaccess__reverse(self):
        url = reverse("team-permissions.request-access", args=[56, "SCHEMEOFWORK.VIEWER"])
        self.assertEqual("/accounts/team-permissions/schemeofwork/56/teacher/SCHEMEOFWORK.VIEWER/request-access", url)


    def test_login_url_resolves_to_account__team_permissions_login(self):
        url = resolve('/accounts/team-permissions/schemeofwork/56/teacher/SCHEMEOFWORK.EDITOR/login')
        self.assertEqual("team-permissions.login-as", url.url_name)
        self.assertEquals(url.func.__name__, TeamPermissionRequestLoginView.__name__)

    
    def test_login_url_resolves_to_account_team_permissions_login__reverse(self):
        url = reverse("team-permissions.login-as", args=[56, "SCHEMEOFWORK.EDITOR"])
        self.assertEqual("/accounts/team-permissions/schemeofwork/56/teacher/SCHEMEOFWORK.EDITOR/login", url)
