from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_schemesofworkkeyword__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__keywords_index__schemeofwork_viewer(self):
       
        testcases = [            
            {
                "route":"keywords.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Computing curriculum for A-Level",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__delete_unpublished__schemeofwork_viewer(self):
        
        testcases = [
            {
                "route":"keywords.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__keywords_new__schemeofwork_viewer(self):
        
        testcases = [
            {
                "route":"keywords.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__keyword_edit__schemeofwork_viewer(self):
        
        testcases = [
            {
                "route":"keywords.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__keyword_save__schemeofwork_viewer(self):
        
        testcases = [
            {
                "route":"keywords.save as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/save",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__keywords_merge__schemeofwork_viewer(self):
        
        testcases = [
            {
                "route":"keywords.merge as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/merge",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__keywords_edit__schemeofwork_editor(self):
        
        testcases = [
            {
                "route":"keywords.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/{self.test_keyword_id}/edit",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Edit keyword: Random Access Memory (RAM) for Computing curriculum for A-Level",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__delete_unpublished__schemeofwork_editor(self):
        
        testcases = [
            {
                "route":"keywords.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }
        ]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")


    def test_page__permission_when__delete_unpublished__schemeofwork_owner(self):

        testcases = [
                {
                "route":"keywords.delete_unpublished as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-owner@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            }]

        self.run_testcases__permission(testcases, "schemeofworkkeywords")