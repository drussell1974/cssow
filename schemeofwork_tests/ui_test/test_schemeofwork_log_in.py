from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ui_testcase import UITestCase

class test_schemeofwork_default(UITestCase):

    test_context = webdriver.Firefox()
    def setUp(self):
        # setup
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/default/user/login")


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # setup

        # test

        # assert
        self.assertWebPageTitleAndHeadings("schemeofwork", "Log In", "Register to create schemes of work and lessons")



    def test_page__login_should_fail_with_incorrect_credentials(self):
        # setup

        # test

        elem = self.test_context.find_element_by_id("auth_user_email")
        elem.send_keys("foobar")
        elem.send_keys(Keys.TAB)

        elem = self.test_context.find_element_by_id("auth_user_password")
        elem.send_keys("password")
        elem.send_keys(Keys.TAB)

        elem.send_keys(Keys.RETURN)

        ' sleep to give time for browser to respond'
        import time
        time.sleep(4)

        # assert
        self.assertEqual("Invalid email", self.test_context.find_element_by_id("email__error").text)

