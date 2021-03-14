from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_schemesofwork__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when_schemeofworks_new__schemeofwork_viewer(self):
        testcases = [            
            {
                "route":"schemesofwork.new as schemeofwork-viewer@localhost should deny",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_delete_unpublished__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_view__schemeofwork_viewer(self):

        testcases = [
            {
                "always_skip": True,
                "skip": True,
                "route":"schemesofwork.view as schemeofwork-viewer@localhost --- NOT IMPLEMENT",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A",
                "exp__subheading":"B",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_edit__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"schemesofwork.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/999999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_publish_item__schemeofwork_viewer(self):

        testcases = [
            {
                "always_skip": True,
                "skip": True,
                "route":"schemesofwork.publish_item as schemeofwork-viewer@localhost ---- publish view NOT IMPLEMENTED",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/999999999/publish",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_index__schemeofwork_viewer(self):

        testcases = [
            {
                "route":"schemesofwork.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_delete_unpublished_schemeofwork_viewer(self):

        testcases = [
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_edit__schemeofwork_editor(self):

        testcases = [
            {
                "route":"schemesofwork.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/edit",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"A-Level Computer Science",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_delete_unpublished__schemeofwork_editor(self):

        testcases = [
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_delete_unpublished__schemeofwork_editor(self):

        testcases = [
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            }]

        self.run_testcases__permission(testcases, "schemeofwork")


    def test_page__permission_when__schemesofwork_delete_unpublished__department_admin(self):

        testcases = [
            {
                "route":"schemesofwork.delete_unpublished as department-admin@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"department-admin@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            },
        ]
        
        self.run_testcases__permission(testcases, "schemeofwork")
        