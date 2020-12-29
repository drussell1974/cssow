from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_keyword_lesson_edit_existing(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/keywords/{}/edit".format(self.test_scheme_of_work_id, self.test_lesson_id, self.test_keyword_id))


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys("")

        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.send_keys("test_page__should_stay_on_same_page_if_invalid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Edit: Random Access Memory (RAM) for Types of CPU architecture')



    def test_page__should_stay_on_same_page_if_renamed_to_create_duplicate(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys(self.TEST_KEYWORD_RENAME_TERM_TO)
        
        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        # TODO: 
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Edit: Central Processing Unit (CPU) for Types of CPU architecture')

        #elem = self.test_context.find_element_by_id("saveButton")
        #self.assertEqual("", elem.text)

        
    def test_page__should_redirect_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys(self.TEST_KEYWORD_TERM)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')

