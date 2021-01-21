from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_learningobjective_pages__permissions_when_different_logged_in_users(UITestCase):

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


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permissions on content
            
        #path('', views.index, name='learningobjective.index'),
        #path('new', views.new, name='learningobjective.new'),
        #path('delete_unpublished', views.delete_unpublished, name='learningobjective.delete_unpublished'),
        #path('<int:learning_objective_id>/edit', views.edit, name='learningobjective.edit'),
        #path('<int:learning_objective_id>/save', views.save, name='learningobjective.save'),
        #path('<int:learning_objective_id>/publish', views.publish_item, name="learningobjective.publish_item")            
        
        """

        testcases = [
            {
                "route":"learningobjective.index",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
            {
                "route":"learningobjective.new",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"learningobjective.delete_unpublished",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"learningobjective.edit",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"learningobjective.save",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/save",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"learningobjective.publish",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/publish",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
        ]
        
        self.run_testcases__permission(testcases, "learningobjective")