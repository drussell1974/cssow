from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_schemesofwork_pages__permissions_when_different_logged_in_users(UITestCase):

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
                "route":"schemesofwork.new",
                "uri":f"/schemesofwork/new",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"schemesofwork.delete_unpublished",
                "uri":f"/schemesofwork/delete_unpublished",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "skip": True,
                "route":"schemesofwork.view",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A",
                "exp__subheading":"B",
            },
            {
                "route":"schemesofwork.edit",
                "uri":f"/schemesofwork/999999999/edit",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "skip": True,
                "route":"schemesofwork.publish_item",
                "uri":f"/schemesofwork/999999999/publish",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"schemesofwork.index",
                "uri":f"/schemesofwork",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"Schemes of Work",
                "exp__subheading":"Our shared schemes of work by key stage",
            },
        ]
        
        self.run_testcases__permission(testcases, "schemeofwork")
        