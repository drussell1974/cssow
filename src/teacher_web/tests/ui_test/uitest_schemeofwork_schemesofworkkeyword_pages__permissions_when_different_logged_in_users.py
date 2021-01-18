from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_schemesofworkkeyword_pages__permissions_when_different_logged_in_users(UITestCase):

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
        
        username = "schemeofwork-viewer@localhost"

        testcases = [

            ## schemeofwork keywords ##
            #path('', views.index, name="keywords.index"),
            #path('delete_unpublished', views.delete_unpublished, name="keywords.delete_unpublished"), 
            #path('new', views.new, name="keywords.new"),
            #path('<int:keyword_id>/edit', views.edit, name="keywords.edit"),
            #path('<int:keyword_id>/delete', views.delete_item, name="keywords.delete_item"), 
            #path('<int:keyword_id>/publish_item', views.publish_item, name="keywords.publish_item"), 
            #path('<int:keyword_id>/save', views.save, name="keywords.save"),
            #path('<int:keyword_id>/merge', views.merge_duplicates, name="keywords.merge_duplicates")
            
            {
                "route":"keywords.index",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords",
                "enter_username":username,
                "allow": True,
                "exp__title":"Dave Russell - Teach Computer Science",
                "exp__h1":"A-Level Computer Science",
                "exp__subheading":"Computing curriculum for A-Level",
            },
            {
                "route":"keywords.delete_unpublished",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords/delete_unpublished",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.new",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords/new",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.edit",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/edit",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.save",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/save",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"keywords.merge",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/keywords/99999999/merge",
                "enter_username":username,
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            
        ]
        
        self.run_testcases__permission(testcases, "schemeofworkkeywords")