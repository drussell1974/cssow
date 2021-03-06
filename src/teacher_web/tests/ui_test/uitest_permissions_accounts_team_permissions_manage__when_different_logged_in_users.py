from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip


class uitest_permissions_accounts_team_permissions_manage__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext(restore_test_data=False)

    def setUp(self):
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permission on team-permissions

        
        """
        
        testcases = [            
            {
                "route":"team-permission.index as schemeofwork-viewer@localhost should deny",
                "uri":f"/accounts/team-permissions/institute/{self.test_institute_id}/department/{self.test_department_id}/",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"team-permission.edit as schemeofwork-viewer@localhost should deny",
                "uri":f"/accounts/team-permissions/institute/{self.test_institute_id}/department/{self.test_department_id }/schemeofwork/{self.test_scheme_of_work_id}/teacher/2/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },            
            
            {
                "route":"team-permission.index as department-admin@localhost should allow",
                "uri":f"/accounts/team-permissions/institute/{self.test_institute_id}/department/{self.test_department_id}/",
                "enter_username":"department-admin@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Account",
                "exp__subheading":"Team Permissions",
            },
            {
                "route":"team-permission.edit as department-admin@localhost should allow",
                "uri":f"/accounts/team-permissions/institute/{self.test_institute_id}/department/{self.test_department_id }/schemeofwork/{self.test_scheme_of_work_id}/teacher/2/edit",
                "enter_username":"department-admin@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Account",
                "exp__subheading":"Team Permissions",
            },
        ]
        
        self.run_testcases__permission(testcases, "team-permissions")
        