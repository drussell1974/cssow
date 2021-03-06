from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_permissions_schemeofwork_schemesofworkkeyword__when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext(restore_test_data=False)

    def setUp(self):
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permission on schemeofwork keywords

        #path('', views.index, name="keywords.index"),
        #path('delete_unpublished', views.delete_unpublished, name="keywords.delete_unpublished"), 
        #path('new', views.new, name="keywords.new"),
        #path('<int:keyword_id>/edit', views.edit, name="keywords.edit"),
        #path('<int:keyword_id>/delete', views.delete_item, name="keywords.delete_item"), 
        #path('<int:keyword_id>/publish_item', views.publish_item, name="keywords.publish_item"), 
        #path('<int:keyword_id>/save', views.save, name="keywords.save"),
        #path('<int:keyword_id>/merge', views.merge_duplicates, name="keywords.merge_duplicates")
        
        """

        testcases = [            
            {
                "route":"keywords.index as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Computing curriculum for A-Level",
            },
            {
                "route":"keywords.delete_unpublished as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.new as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.edit as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.save as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/save",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.merge as schemeofwork-viewer@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/merge",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"keywords.edit as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/{self.test_keyword_id}/edit",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": True,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Edit keyword: Random Access Memory (RAM) for Computing curriculum for A-Level",
            },
            {
                "route":"keywords.delete_unpublished as schemeofwork-editor@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-editor@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },


            {
                "route":"keywords.delete_unpublished as schemeofwork-owner@localhost",
                "uri":f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":"schemeofwork-owner@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            },
            
        ]
        
        self.run_testcases__permission(testcases, "schemeofworkkeywords")