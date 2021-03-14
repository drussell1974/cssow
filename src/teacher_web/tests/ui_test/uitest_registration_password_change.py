from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_registration_password_change(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.try_log_in(self.root_uri + "/accounts/password_change", wait=4)


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

        ' old password '
        elem = self.test_context.find_element_by_id("id_old_password")
        elem.clear()
        elem.send_keys("password1.")

        ' new password '
        elem = self.test_context.find_element_by_id("id_new_password1")
        elem.clear()
        elem.send_keys("password1.")

        ' confirm new password '
        elem = self.test_context.find_element_by_id("id_new_password2")
        elem.clear()
        elem.send_keys("password1.")

        ' submit '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_element_by_css_selector(".maincontent h1")
        self.assertEqual("Password changed", elem.text)

        self.assertWebPageTitleAndHeadings('', 'Account', 'Password changed')


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        elem = self.test_context.find_element_by_id("id_old_password")
        elem.clear()

        elem = self.test_context.find_element_by_id("id_new_password1")
        elem.clear()

        elem = self.test_context.find_element_by_id("id_new_password2")
        elem.clear()

        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_elements_by_xpath("/html/body/div/div/div[3]/div/h1")
        self.assertEqual("Change password", elem[0].text)

        self.assertWebPageTitleAndHeadings('', 'Account', 'Change password')

