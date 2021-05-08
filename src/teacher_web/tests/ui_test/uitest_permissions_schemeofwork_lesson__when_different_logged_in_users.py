from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_lesson__when_different_logged_in_users(UITestCase):

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


    def test_page__permission_when__lesson_index__schemeofwork_viewer(self):
        testcases = [            
            {
                "route":"lesson.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Scheme of work",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__delete_unpublished__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_new__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_edit__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_copy__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.copy as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/copy",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_publish__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.publish as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/99999999/copy",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_whiteboard__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"lesson.whiteboard as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/schedules/{self.test_lesson_schedule_id}/whiteboard",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Algorithms",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__lesson_edit__schemeofwork_editor(self):

        testcases = [
            {
                "route":"lesson.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/edit",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Scheme of work",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__delete_unpublished__schemeofwork_editor(self):

        testcases = [
            {
                "route":"lesson.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/delete_unpublished",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "lesson")


    def test_page__permission_when__delete_unpublished__schemeofwork_owner(self):

        testcases = [
            {
                "route":"lesson.delete_unpublished as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/delete_unpublished",
                "enter_username": "schemeofwork-owner@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Scheme of work",
            },
        ]
        
        
        self.run_testcases__permission(testcases, "lesson")