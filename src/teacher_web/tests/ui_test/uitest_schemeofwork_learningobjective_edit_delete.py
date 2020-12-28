from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_learningobjective_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):

        #self.test_context.implicitly_wait(10)
        # setup
        #231: create a new learning objective
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/learning-objectives/new".format(self.test_scheme_of_work_id, self.test_lesson_id))

        # create learning objective

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
        elem.send_keys("uitest_schemeofwork_learningobjective_edit_delete")

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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_redirect_to_index_after_deletion(self):

        #delete

        ' Open edit '
        self.delete_unpublished_item(".unpublished .edit .post-title")

        
        self.wait(s=5)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        
        items_after = self.test_context.find_elements_by_class_name("post-preview")
        
        #231: items after should be less than before
        
        self.assertEqual(8, len(items_after))
