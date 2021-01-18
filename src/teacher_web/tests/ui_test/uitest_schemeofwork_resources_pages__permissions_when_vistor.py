from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_resources_pages__permissions_when_vistor(UITestCase):

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

        #path('', views.index, name="resource.index"),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):

        #path('delete_unpublished', views.delete_unpublished, name="resource.delete_unpublished"), 
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__new__should_redirect_to_login_when_with_permission_error(self):

        #path('new', views.new, name="resource.new"),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:resource_id>/edit', views.edit, name="resource.edit"),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/99999999/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:resource_id>/delete', views.delete_item, name="resource.delete_item"), 
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/99999999/delete")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__publish__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:resource_id>/publish_item', views.publish_item, name="resource.publish_item"), 
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/99999999/publish_item")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__save__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:resource_id>/save', views.save, name="resource.save")
        #         
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/99999999/save")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")



