from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_default(UITestCase):

    test_context = webdriver.Firefox()
    def setUp(self):
        # set up
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/default/index")

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
        self.assertWebPageTitleAndHeadings("schemeofwork", "Computing Schemes of work and lessons", "Computing schemes of work lessons across all key stages")


    def test_page__login_should_redirect_to_default_index(self):
        # setup

        # test
        self.test_context.find_element_by_id("btn-login").click()

        ' sleep to give time for browser to respond '
        import time
        time.sleep(3)

        elem = self.test_context.find_element_by_id("auth_user_email")
        elem.send_keys("dave@jazzthecat.co.uk")
        elem.send_keys(Keys.TAB)

        elem = self.test_context.find_element_by_id("auth_user_password")
        elem.send_keys("co2m1c")
        elem.send_keys(Keys.RETURN)

        ' sleep to give time for browser to respond '
        import time
        time.sleep(3)

        # assert
        ' redirect back to home page '
        self.assertWebPageTitleAndHeadings("schemeofwork", "Computing Schemes of work and lessons", "Computing schemes of work lessons across all key stages")







