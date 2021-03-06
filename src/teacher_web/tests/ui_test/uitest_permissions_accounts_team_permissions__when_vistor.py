from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip
      
class uitest_permissions_accounts_team_permissions__when_vistor(UITestCase):

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


    def test_page__index__should_redirect_to_login_when_with_permission_error(self):

        #path("", views.index, name="team-permissions.index"),
        
        # test
        self.try_log_out(f"/accounts/team-permissions/")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):

        #path("", views.index, name="team-permissions.edit"),
        
        # test
        self.try_log_out(f"/accounts/team-permissions/schemeofwork/99/teacher/101/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete__should_redirect_to_login_when_with_permission_error(self):

        #path("delete", views.delete, name="team-permissions.delete")
                
        # test
        self.try_log_out(f"/accounts/team-permissions/schemeofwork/99/teacher/101/delete")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")
