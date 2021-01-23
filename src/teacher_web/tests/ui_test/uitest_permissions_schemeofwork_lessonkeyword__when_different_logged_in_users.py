from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_lessonkeyword__when_different_logged_in_users(UITestCase):

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
        """ test permission on lesson keywords
                
        path('', views.index, name="lesson_keywords.index"),
        path('delete_unpublished', views.delete_unpublished, name="lesson_keywords.delete_unpublished"), 
        path('select', views.select, name="lesson_keywords.select"),
        path('new', views.new, name="lesson_keywords.new"),
        path('<int:keyword_id>/edit', views.edit, name="lesson_keywords.edit"),
        path('<int:keyword_id>/delete', views.delete_item, name="lesson_keywords.delete_item"), 
        path('<int:keyword_id>/publish_item', views.publish_item, name="lesson_keywords.publish_item"), 
        path('<int:keyword_id>/save', views.save, name="lesson_keywords.save")
        
        """
        
        testcases = [           
            {
                "route":"lesson_keywords.index as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
            {
                "route":"lesson_keywords.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.select as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/select",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.new as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.edit as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.delete as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/delete",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.publish_item as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/publish_item",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"lesson_keywords.save as schemeofwork-viewer@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/save",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            


            {
                "route":"lesson_keywords.edit as schemeofwork-editor@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/{self.test_keyword_id}/edit",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Edit: Random Access Memory (RAM) for Types of CPU architecture",
            },
            {
                "route":"lesson_keywords.publish_item as schemeofwork-owner@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/{self.test_keyword_id}/publish_item",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"lesson_keywords.publish_item as schemeofwork-owner@localhost",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/delete_unpublished",
                "enter_username": "schemeofwork-owner@localhost",
                "allow": True,
                "wait_for_element_id": "index-page--group-heading",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
        ]
        
        self.run_testcases__permission(testcases, "lessonkeywords")