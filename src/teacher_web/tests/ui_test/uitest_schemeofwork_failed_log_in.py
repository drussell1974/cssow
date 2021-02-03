from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_failed_log_in(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/schemesofwork")
        self.test_context.implicitly_wait(4)

        try:
            elem = self.test_context.find_element_by_id("btn-logout")
            elem.click()
        except:
            pass # ignore errors as may already be logged out

        self.wait(s=2)
        

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__login_should_fail_with_incorrect_credentials(self):

        # setup
        self.test_context.find_element_by_id("btn-login").click()

        # test

        elem = self.test_context.find_element_by_id("id_username")
        elem.send_keys("foo")
        elem.send_keys(Keys.TAB)

        elem = self.test_context.find_element_by_id("id_password")
        elem.send_keys("bar")
        elem.send_keys(Keys.TAB)

        elem.send_keys(Keys.RETURN)

        # assert
        self.assertEqual("Your username and password didn't match. Please try again.", self.test_context.find_element_by_id("login_error").text)
