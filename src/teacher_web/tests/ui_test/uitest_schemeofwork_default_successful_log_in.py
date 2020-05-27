import sys

sys.path.append('../')

from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_successful_log_in(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + "/schemesofwork")
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__login_should_redirect_to_default_index__with_correct_credentials(self):

        # assert
        ' redirect back to home page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')

        elem = self.test_context.find_element_by_id("btn-profile")
        self.assertEqual("test@localhost", elem.text)

        elem = self.test_context.find_element_by_id("btn-logout")
        self.assertEqual("Logout", elem.text)


    def test_page_navigate_to_default_index_after_log_out(self):
        # set up
        self.try_log_in(self.root_uri + "/schemesofwork")

        # test
        self.test_context.find_element_by_id('btn-logout').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')

        elem = self.test_context.find_element_by_id("btn-login")
        self.assertEqual("Login", elem.text)
        