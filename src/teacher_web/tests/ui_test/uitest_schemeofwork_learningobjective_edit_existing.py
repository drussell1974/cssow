from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_learningobjective_edit_existing(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        #231: published item
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/{self.test_learning_objective_id}/edit")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
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
        elem = self.test_context.find_element_by_id("ctl-description")
        elem.clear()
        elem.send_keys("")

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Edit: Explain what happens to inactive processes and what is the purpose of managing these inactive processes')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        
        elem = self.test_context.find_element_by_id("saveButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        
        ' submit the form '
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC', wait=4)


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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Create new resource for Types of CPU architecture')