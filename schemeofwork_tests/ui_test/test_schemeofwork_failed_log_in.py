from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ui_testcase import UITestCase

class test_schemeofwork_failed_log_in(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/default/index")
        self.test_context.implicitly_wait(4)


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

        elem = self.test_context.find_element_by_id("auth_user_email")
        elem.send_keys("foobar")
        elem.send_keys(Keys.TAB)

        elem = self.test_context.find_element_by_id("auth_user_password")
        elem.send_keys("password")
        elem.send_keys(Keys.TAB)

        elem.send_keys(Keys.RETURN)

        # assert
        self.assertEqual("Invalid email", self.test_context.find_element_by_id("email__error").text)
