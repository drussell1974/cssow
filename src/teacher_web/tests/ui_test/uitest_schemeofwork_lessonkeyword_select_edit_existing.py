from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lessonkeyword_select_edit_existing(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/select", wait=2)


    def tearDown(self):

        elem = self.test_context.find_elements_by_class_name("post-preview")
        
        # if the test has left less than 3 items then restore test_keyword_id
        if len(elem) < 3:           
            
            self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/select", wait=2)

            elem = self.test_context.find_element_by_id("chk-term--{}".format(self.test_keyword_id))
            ' Ensure element is visible '
            self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
            self.wait(s=2)
            
            # act
            
            ' select term '

            elem.click()

            ' submit the form '
            elem = self.test_context.find_element_by_id("saveButton")

            self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
            
            elem.send_keys(Keys.RETURN)
            print("KEYWORD RESTORED!!!!")
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    @skip("not use case for validation")
    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Create new keyword for Types of CPU architecture')
        

    def test_page__should_redirect_to_index_if_valid(self):
        # setup

        elem = self.find_element_by_id__with_explicit_wait("chk-term--{}".format(self.test_keyword_id))
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        
        # act
        
        ' select term '

        elem.click()

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")

        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        elem.send_keys(Keys.RETURN)

        self.wait(s=1)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')

        elem = self.test_context.find_elements_by_class_name("card-keyword")
        self.assertEqual(2, len(elem))
