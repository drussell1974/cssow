from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.try_log_in(self.root_uri + "/accounts")

        self.test_context.implicitly_wait(4)
        self.wait(s=2)

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_have_password_reset(self):
        
        # arrange
        elem = self.test_context.find_element_by_class_name("maincontent h1")

        self.assertEqual("test@localhost", elem.text)


