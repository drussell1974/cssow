from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_permissions_schemeofwork_content__when_vistor(UITestCase):

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


    def test_page__index__should_redirect_to_login_with_permission_error(self):
        
        #path('', views.index, name="content.index"),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__new__should_redirect_to_login_with_permission_error(self):
        
        #path('new', views.edit, name="content.new"),
        
        # act
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__edit__should_redirect_to_login_with_permission_error(self):
        
        #path('<int:content_id>/edit', views.edit, name="content.edit"),        
        
        # act
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/999999/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")

        
