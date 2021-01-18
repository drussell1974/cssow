from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_learningobjective_pages__public_permissions(UITestCase):

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

        #path('', views.index, name='learningobjective.index'),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")
        

    def test_page__new__should_redirect_to_login_when_with_permission_error(self):

        #path('new', views.new, name='learningobjective.new'),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/new")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__delete_unpublished__should_redirect_to_login_when_with_permission_error(self):

        #path('delete_unpublished', views.delete_unpublished, name='learningobjective.delete_unpublished'),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/delete_unpublished")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__edit__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:learning_objective_id>/edit', views.edit, name='learningobjective.edit'),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/edit")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__save__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:learning_objective_id>/save', views.save, name='learningobjective.save'),
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/save")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")


    def test_page__publish_item__should_redirect_to_login_when_with_permission_error(self):

        #path('<int:learning_objective_id>/publish', views.publish_item, name="learningobjective.publish_item")
        
        # test
        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/publish")
        
        # assert
        self.assertLoginPage(login_message="Enter your email and password", exception_message="PermissionError at")
