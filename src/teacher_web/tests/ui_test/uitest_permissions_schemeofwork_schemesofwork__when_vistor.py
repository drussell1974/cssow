from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_permissions_schemeofwork_schemesofwork__when_vistor(UITestCase):

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
        #path('<int:scheme_of_work_id>', views.index, name='schemesofwork.view'),    
        #path('', views.index, name='schemesofwork.index'),
        # test
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork", enter_username="schemeofwork-viewer@localhost", wait=5)
        
        # assert
        self.assertWebPageTitleAndHeadings(title="Dave Russell - Teach Computer Science", h1="Computer Science", subheading="Department", should_be_logged_in=True, username="View Scheme of work only")


    def test_page__new__should_redirect_to_login_when_with_permission_error(self):
        #path('new', views.edit, name='schemesofwork.new'),
        # test
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/new")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):
        #path('<int:scheme_of_work_id>/edit', views.edit, name='schemesofwork.edit'),
        # test
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/11/edit")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):
        #path('delete_unpublished', views.delete_unpublished, name="schemesofwork.delete_unpublished"),
        # test
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at /schemesofwork/delete_unpublished")
