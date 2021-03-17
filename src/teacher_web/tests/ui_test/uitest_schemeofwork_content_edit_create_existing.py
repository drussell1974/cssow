from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_content_edit_create_existing(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/{self.test_content_id}/edit")


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
        elem = self.test_context.find_element_by_id("ctl-letter_prefix")
        elem.clear()
        elem.send_keys("")

        elem = self.test_context.find_element_by_id("ctl-description")
        elem.send_keys("test_page__should_stay_on_same_page_if_invalid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Edit: data representation')

        elem.click()


    def test_page__should_redirect_to_next_if_valid(self):
        ''' Test Next option '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        
        elem = self.test_context.find_element_by_css_selector("#wizard-options > option:nth-child(2)")
        elem.click()
        self.wait(s=1)
        
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should be next page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new keyword for A-Level Computer Science')