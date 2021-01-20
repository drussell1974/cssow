from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_register_new_when_logged_in(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.do_log_in(self.root_uri + "/accounts/register")
        

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_show_already_registered_when_logged_in(self):
        
        # arrange
        elem = self.test_context.find_element_by_css_selector(".maincontent h1")

        self.assertEqual("You are already registered", elem.text)


