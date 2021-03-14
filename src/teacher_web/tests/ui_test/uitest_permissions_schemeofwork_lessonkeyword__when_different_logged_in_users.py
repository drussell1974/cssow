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


    def test_page__permission_when__keywords_index__schemeofwork_viewer(self):
        
        testcases = [           
            {
                "route":"lesson_keywords.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__delete_unpublished__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_select__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.select as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/select",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_new__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_edit__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_delete__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.delete as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/delete",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_publish_item__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.publish_item as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/publish_item",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_save__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson_keywords.save as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/keywords/999999999/save",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_edit_item__schemeofwork_editor(self):

        testcases = [
            {
                "route":"lesson_keywords.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/{self.test_keyword_id}/edit",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Edit: Random Access Memory (RAM) for Types of CPU architecture",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_publish_item__schemeofwork_editor(self):

        testcases = [
            {
                "route":"lesson_keywords.publish_item as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/{self.test_keyword_id}/publish_item",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lessonkeywords")


    def test_page__permission_when__keywords_publish_item__schemeofwork_owner(self):

        testcases = [
            {
                "route":"lesson_keywords.publish_item as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/delete_unpublished",
                "enter_username": "schemeofwork-owner@localhost",
                "allow": True,
                "wait_for_element_id": "index-page--group-heading",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Von Neumann architecture and Harvard architecture, and CISC and RISC",
            },
        ]
        
        self.run_testcases__permission(testcases, "lessonkeywords")