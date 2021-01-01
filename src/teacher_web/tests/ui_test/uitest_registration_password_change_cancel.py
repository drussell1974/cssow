from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_registration_password_reset_cancel(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.try_log_in(self.root_uri + "/accounts/password_change")

        self.test_context.implicitly_wait(4)


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

        ' Open Modal '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')

