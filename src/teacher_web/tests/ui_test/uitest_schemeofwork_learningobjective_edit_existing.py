from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_learningobjective_edit_existing(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        #231: published item
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/learning-objectives/{}/edit".format(self.test_scheme_of_work_id, self.test_lesson_id, self.test_learning_objective_id))


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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
