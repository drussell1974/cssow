from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_default(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork")
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__login_should_redirect_to_default_index__with_correct_credentials(self):
        # setup

        self.test_context.find_element_by_id("btn-login").click()

        # test

        elem = self.test_context.find_element_by_id("auth_user_email")
        elem.send_keys("test@localhost")
        elem.send_keys(Keys.TAB)

        elem = self.test_context.find_element_by_id("auth_user_password")
        elem.send_keys("co2m1c")
        elem.send_keys(Keys.RETURN)

        # assert
        ' redirect back to home page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')


    def test_page_navigate_to_default_index_after_log_out(self):
        # set up
        self.try_log_in('http://dev.computersciencesow.net:8000/schemeofwork/schemesofwork/index')

        # test
        self.test_context.find_element_by_id('btn-logout').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')
