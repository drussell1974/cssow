from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_eventlog_pages__permissions_when_vistor(UITestCase):

    test_context = WebBrowserContext()

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

        #path("", views.index, name="eventlog.index"),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/event-log")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete__should_redirect_to_login_when_with_permission_error(self):

        #path("delete", views.delete, name="eventlog.delete")
                
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/event-log/delete")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")
