from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_learningobjective_edit_create_new(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/learning-objectives/new".format(self.test_scheme_of_work_id, self.test_lesson_id))


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

        ' ctl-solo_taxonomy_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-solo_taxonomy_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Multistructural: Describe, List (give an account or give examples of)":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-description")
        elem.clear()
        elem.send_keys("")

        ' ctl-content_id SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-content_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "fundamentals of programming":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'New')
        

    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-solo_taxonomy_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-solo_taxonomy_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Multistructural: Describe, List (give an account or give examples of)":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' description '

        elem = self.test_context.find_element_by_id("ctl-description")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' ctl-content_id SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-content_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "fundamentals of programming":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' group_name Enter Valid '

        elem = self.test_context.find_element_by_id("ctl-group_name")
        elem.clear()
        elem.send_keys("Loerm ipsum dol")
        
        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture\; CISC and RISC')

        #delete
        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()
