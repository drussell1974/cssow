from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofwork_pages__public_permissions(UITestCase):

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


    def test_page__index__should_be_allowed(self):
        # test
        self.do_log_in(f"/schemesofwork", enter_username="schemeofwork-viewer@localhost", wait=5)
        
        # assert
        self.assertWebPageTitleAndHeadings(title="Dave Russell - Teach Computer Science", h1="Schemes of Work", subheading="Our shared schemes of work by key stage", should_be_logged_in=True, username="View Scheme of work only")


    def test_page__new__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/new")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/edit")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/delete_unpublished")
