from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_lesson_page_permission(UITestCase):

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


    def test_page__index_should_redirect_to_login_when_with_permission_error_when_public_user(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons")
        
        # assert
        self.assertCustomPermissionDenied(h1="PermissionError at /schemesofwork/11/lessons/")


    def test_page__new_should_redirect_to_login_when_with_permission_error_when_public_user(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/new")
        
        # assert
        self.assertLoginPage()


    def test_page__edit_should_redirect_to_login_when_with_permission_error_when_public_user(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/edit")
        
        # assert
        #self.assertCustomPermissionDenied(h1="PermissionError at VERIFY")
        self.assertLoginPage()
