from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_registration_password_reset_cancel(UITestCase):

    test_context = WebBrowserContext(restore_test_data=False)

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
    
    def test_page__should_stay_on_same_page_if_stay(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' enter something before cancelling '
        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("test@loca...")

        ' cancel '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')

