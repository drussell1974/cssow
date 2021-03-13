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


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permission on schemeofwork

        path('new', views.edit, name='schemesofwork.new'),
        path('delete_unpublished', views.delete_unpublished, name="schemesofwork.delete_unpublished"),
        path('<int:scheme_of_work_id>', views.index, name='schemesofwork.view'),    
        path('<int:scheme_of_work_id>/edit', views.edit, name='schemesofwork.edit'),
        path('<int:scheme_of_work_id>/publish', views.index, name='schemesofwork.publish_item'),
        path('', views.index, name='schemesofwork.index'), 
        
        """
        
        testcases = [            
            {
                "route":"schemesofwork.new as schemeofwork-viewer@localhost should deny",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
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
            },
            {
                "route":"schemesofwork.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/999999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "always_skip": True,
                "skip": True,
                "route":"schemesofwork.publish_item as schemeofwork-viewer@localhost ---- publish view NOT IMPLEMENTED",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/999999999/publish",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"schemesofwork.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            },
            
            
            {
                "route":"schemesofwork.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/edit",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"A-Level Computer Science",
            },
            {
                "route":"schemesofwork.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },

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
        