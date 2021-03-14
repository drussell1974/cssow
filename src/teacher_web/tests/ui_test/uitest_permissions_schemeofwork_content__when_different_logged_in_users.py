from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_content__when_different_logged_in_users(UITestCase):

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


    def test_page__permission_when__content_index__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"content.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Curriculum",
            }        ]

        self.run_testcases__permission(testcases, "content")


    def test_page__permission_when__content_new__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"content.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }        ]

        self.run_testcases__permission(testcases, "content")


    def test_page__permission_when__content_edit__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"content.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/99999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }        ]

        self.run_testcases__permission(testcases, "content")


    def test_page__permission_when__delete_unpublished__schemeofwork_viewer(self):

        testcases = [    
            {
                "route":"content.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/99999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "content")


    def test_page__permission_when__content_edit__schemeofwork_editor(self):

        testcases = [
            {
                "route":"content.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/{self.test_content_id}/edit",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Edit: data representation",
            }
        ]

        self.run_testcases__permission(testcases, "content")


    def test_page__permission_when__delete_unpublished__schemeofwork_owner(self):

        testcases = [
            {
                "route":"content.delete_unpublished as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/delete_unpublished",
                "enter_username":"schemeofwork-owner@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Curriculum",
            },
        ]
        
        self.run_testcases__permission(testcases, "content")