from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

@skip("TODO: #206 check if javascript is not triggering the filtering when automated.")
class uitest_schemeofwork_schemesofworkkeyword_index__search_term(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in("/schemesofwork/{}/keywords".format(self.test_scheme_of_work_id), print_uri=False)
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_all_by_default(self):
        # test
        elem = self.test_context.find_elements_by_xpath("//*[contains(@class, 'card card-keyword')]")
        
        # assert
        self.assertEqual(155, len(elem))


    def test_page__should_show_none(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("abcd")
        
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        
        # assert
        self.assertEqual(0, len(elem))


    def test_page__should_upper_and_lower_case_matches(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("Ram")
        elem.send_keys(Keys.ENTER)
        self.wait(s=1)
        
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        
        # assert
        self.assertEqual(2, len(elem))


    def test_page__should_single_item_match(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("Random Access Memory (RAM)")
        elem.send_keys(Keys.ENTER)
        self.wait(s=1)
        
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'display: block')]")
        
        # assert
        self.assertEqual(1, len(elem))