from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_registration_password_reset_request_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # ensure test user is logged out for this test

        try:
            elem = self.test_context.find_element_by_id("btn-logout")
            elem.click()
        except:
            pass # ignore errors as may already be logged out


        self.test_path = "/accounts/password_reset"
        self.do_get(self.root_uri + self.test_path, wait=4)


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_direct_to_reset_sent(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        elem = self.test_context.find_element_by_id("id_email")
        elem.send_keys("test@localhost")

        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_element_by_css_selector(".maincontent h1")
        self.assertEqual("Password reset request sent", elem.text)

        self.assertWebPageTitleAndHeadings('', 'Registration', 'Reset password')


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()

        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_elements_by_xpath("/html/body/div/div/div[3]/div/h1")
        self.assertEqual("Forgot your password?", elem[0].text)

        self.assertWebPageTitleAndHeadings('', 'Registration', 'Reset your password')

