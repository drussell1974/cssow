from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofworkkeyword_edit_existing(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/{self.test_keyword_id}/edit", wait=6)


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
        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Edit keyword: Random Access Memory (RAM) for Computing curriculum for A-Level')


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
        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new keyword for A-Level Computer Science')
        
        
    def test_page__should_redirect_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)
        
        ' submit the form '
        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')

        #delete
        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()


    def test_page__should_redirect_to_next_if_valid(self):
        ''' Test Next option '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        
        elem = self.find_wizardoptions_element_by_id("saveButtonNext")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should be next page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new lesson for A-Level Computer Science')