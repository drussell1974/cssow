from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofwork_index(UITestCase):

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


    def test_page__when_public_user___should_redirect_to_login_with_permission_error(self):
        # test
        

        self.try_log_out(f"/schemesofwork/{self.test_scheme_of_work_id}/lessons")
        
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
