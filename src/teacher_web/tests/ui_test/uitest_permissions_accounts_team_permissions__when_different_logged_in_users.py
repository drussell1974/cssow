from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_accounts_team_permissions__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext(restore_test_data=False)

    def setUp(self):
        # set up
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permission on team-permissions

        #path("", views.index, name="team-permissions.index"),
        #path("edit", views.edit, name="team-permissions.edit")
        #path("delete", views.delete, name="team-permissions.delete")

        """

        testcases = [
            {
                "route":"team-permissions.index as schemeofwork-viewer@localhost",
                "uri":f"/accounts/team-permissions",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"team-permissions.edit as schemeofwork-viewer@localhost",
                "uri":f"/accounts/team-permissions/schemeofwork/{self.test_scheme_of_work_id}/teacher/101/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"team-permissions.index as schemeofwork-editor@localhost",
                "uri":f"/accounts/team-permissions",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Account",
                "exp__subheading":"Team Permissions",
            },  
            {
                "route":"team-permissions.delete as schemeofwork-editor@localhost",
                "uri":f"/accounts/team-permissions/schemeofwork/{self.test_scheme_of_work_id}/teacher/5/delete",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },  


            {
                "route":"team-permissions.delete as drussell1974",
                "uri":f"/accounts/team-permissions/schemeofwork/{self.test_scheme_of_work_id}/teacher/5/delete",
                "enter_username":"drussell1974",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Account",
                "exp__subheading":"Team Permissions",
            },  
        ]
        
        self.run_testcases__permission(testcases, "teampermissions")
