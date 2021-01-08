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
        try:
            elem = self.test_context.find_element_by_id("btn-logout")
            elem.click()
        except:
            pass # ignore errors as may already be logged out

        self.test_context.get(self.root_uri + f"/schemesofwork/{self.test_scheme_of_work_id}/lessons")
        self.test_context.implicitly_wait(4)
        
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
