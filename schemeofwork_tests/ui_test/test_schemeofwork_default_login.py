from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ui_testcase import UITestCase

class test_schemeofwork_default_login(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/default/user/login")


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # setup
        self.test_context.find_element_by_id("btn-login").click()

        ' sleep to give time for browser to respond '
        import time
        time.sleep(3)

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('default/user/login')

