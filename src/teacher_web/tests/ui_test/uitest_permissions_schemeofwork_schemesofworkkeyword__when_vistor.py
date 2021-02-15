from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse
import unittest

class uitest_permissions_schemeofwork_schemesofworkkeyword__when_vistor(UITestCase):

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
        
        #path('', views.index, name="keywords.index"),

        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__new__should_redirect_to_login_when_with_permission_error(self):
        
        #path('new', views.new, name="keywords.new"),
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:keyword_id>/edit', views.edit, name="keywords.edit"),
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):

        #path('delete_unpublished', views.delete_unpublished, name="keywords.delete_unpublished"), 
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError")


    def test_page__delete__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:keyword_id>/delete', views.delete_item, name="keywords.delete_item"), 

        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/delete")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError")


    def test_page__publish__should_redirect_to_login_when_with_permission_error(self):
        
        #path('<int:keyword_id>/publish_item', views.publish_item, name="keywords.publish_item"), 
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/publish_item")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__save__should_redirect_to_login_when_with_permission_error(self):
        #path('<int:keyword_id>/save', views.save, name="keywords.save"),
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/save")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__merge__should_redirect_to_login_when_with_permission_error(self):
        #path('<int:keyword_id>/merge', views.merge_duplicates, name="keywords.merge_duplicates")  
        
        # act
        self.try_log_out(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/merge")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")      
