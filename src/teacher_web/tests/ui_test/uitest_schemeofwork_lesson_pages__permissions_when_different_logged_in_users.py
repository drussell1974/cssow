from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lesson_pages__permissions_when_different_logged_in_users(UITestCase):

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
        """ test permissions on lessons
            
        #path('', views.index, name="lesson.index"),
        #path('delete_unpublished', views.delete_unpublished, name="lesson.delete_unpublished"), 
        #path('new', views.edit, name="lesson.new"),
        #path('<int:lesson_id>', views.index, name="lesson.view"),
        #path('<int:lesson_id>/edit', views.edit, name="lesson.edit"),
        #path('<int:lesson_id>/copy', views.edit, { "is_copy": True }, name="lesson.copy"), 
        #path('<int:lesson_id>/publish', views.publish, name="lesson.publish_item"), 
        #path('<int:lesson_id>/whiteboard', views.whiteboard, name="lesson.whiteboard_view"),
        
        """

        testcases = [            
            {
                "route":"lesson.index",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Lessons",
            },
            {
                "route":"lesson.delete_unpublished",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson.new",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson.edit",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson.copy",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/copy",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson.publish",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/copy",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson.whiteboard",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/whiteboard",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Algorithms",
            },
        ]
        
        self.run_testcases__permission(testcases, "lesson")