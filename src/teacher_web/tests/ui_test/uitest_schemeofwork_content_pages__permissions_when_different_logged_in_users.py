from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_content_pages__permissions_when_different_logged_in_users(UITestCase):

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
        
        username = "schemeofwork-viewer@localhost"

        testcases = [
            
            ## content ##
            
            #path('', views.index, name="content.index"),
            #path('new', views.edit, name="content.new"),
            #path('<int:content_id>/edit', views.edit, name="content.edit"),
            
            {
                "route":"content.index",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content",
                "enter_username":username,
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Curriculum",
            },
            {
                "route":"content.new",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/new",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"content.edit",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/99999999/edit",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },            
        ]
        
        self.run_testcases__permission(testcases, "content")