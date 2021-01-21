from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_eventlog_pages__permissions_when_different_logged_in_users(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up

        #path("", views.index, name="eventlog.index"),
        #path("delete", views.delete, name="eventlog.delete")

        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__permission_when__schemeofwork_viewer(self):
        """ test permission on event-logs

        #path("", views.index, name="eventlog.index"),
        #path("delete", views.delete, name="eventlog.delete")

        """

        testcases = [
            {
                "route":"eventlog.index",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/event-log",
                "enter_username": "schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },
            {
                "route":"eventlog.delete",
                "uri":f"/schemesofwork/{self.test_scheme_of_work_id}/event-log/delete",
                "enter_username":"schemeofwork-viewer@localhost",
                "allow": False,
                "exp__login_message":"The item is currently unavailable or you do not have permission.",
            },    
        ]
        
        self.run_testcases__permission(testcases, "eventlog")
