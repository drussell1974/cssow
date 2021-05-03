from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lessonks123pathway_select_edit_existing(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/pathways/select", wait=2)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        
        elem = self.find_element_by_id__with_explicit_wait("ctl-pathway_ks123--{}".format(self.test_ks123pathway_id))
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=4)
        # act
        
        ' select term '

        elem.click()

        ' submit the form '
        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        self.wait(s=2)

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lesson', wait=2)


    def test_page__should_redirect_to_next_if_valid(self):
        # setup

        elem = self.find_element_by_id__with_explicit_wait("ctl-pathway_ks123--{}".format(self.test_ks123pathway_id))
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        
        # act
        
        ' select term '

        elem.click()

        ' submit the form '

        elem = self.find_wizardoptions_element_by_id("saveButtonNext")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Lesson', wait=2)
