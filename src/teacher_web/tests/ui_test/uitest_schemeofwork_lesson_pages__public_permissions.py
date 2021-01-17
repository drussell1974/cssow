from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lesson_pages__public_permissions(UITestCase):

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
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/lessons/")


    def test_page__new__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/lessons/new")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/lessons/220/edit")


    def test_page__publish__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/publish")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/lessons/220/publish")


    def test_page__whiteboard__should_be_allowed(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/whiteboard")
        
        # assert
        self.assertWebPageTitleAndHeadings(title="Dave Russell - Teach Computer Science", h1="Types of CPU architecture", subheading="Algorithms")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/delete_unpublished")

