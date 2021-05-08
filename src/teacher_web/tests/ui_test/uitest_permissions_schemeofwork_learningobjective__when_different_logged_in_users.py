from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_learningobjective__when_different_logged_in_users(UITestCase):

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


    def test_page__permission_when__learningobjective_index__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Lesson",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_new__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/new",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_delete_unpublished__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/delete_unpublished",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_edit__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/edit",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_save__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.save as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/save",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_publish__schemeofwork_viewer(self):
        testcases = [
            {
                "route":"learningobjective.publish as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/99999999/publish",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_edit__schemeofwork_editor(self):
        testcases = [
            {
                "route":"learningobjective.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/{self.test_learning_objective_id}/edit",
                "enter_username": "schemeofwork-editor@localhost",
                "allow":True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Types of CPU architecture",
                "exp__subheading":"Lesson",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__learningobjective_delete__schemeofwork_editor(self):

        testcases = [
            {
                "route":"learningobjective.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/delete_unpublished",
                "enter_username": "schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "learningobjective")


    def test_page__permission_when__event_log_index__schemeofwork_editor(self):

        testcases = [
            {
                "route": "learningobjective.publish as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/{self.test_learning_objective_id}/publish",
                "enter_username": "schemeofwork-owner@localhost",
                "allow": True,
                "exp__title": "Dave Russell - Teach Computer Science",
                "exp__h1": "Types of CPU architecture",
                "exp__subheading": "Lesson",
            },
        ]
        
        self.run_testcases__permission(testcases, "learningobjective")
