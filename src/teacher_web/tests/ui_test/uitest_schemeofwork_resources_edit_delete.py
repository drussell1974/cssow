from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_resources_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):

        #self.test_context.implicitly_wait(10)
        # setup
        #231: create a new resource
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/resources/new".format(self.test_scheme_of_work_id, self.test_lesson_id))

         # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        #self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' ctl-uri '
        elem = self.test_context.find_element_by_id("ctl-uri")
        elem.send_keys("https://www.pgonline.co.uk/resources/computer-science/a-level-ocr/ocr-a-level-textbook/")
        
        ' ctl-publisher '
        elem = self.test_context.find_element_by_id("ctl-publisher")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Markdown")

        ' ctl-md_document_name '
        elem = self.test_context.find_element_by_id("ctl-md_file")
        import os
        test_file = "{}/README.md".format(os.getcwd())
        elem.send_keys(test_file)

        ' ctl-notes '
        elem = self.test_context.find_element_by_id("ctl-notes")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mollis ligula dui, quis feugiat elit hendrerit condimentum. Mauris dignissim ultrices.")

        ' submit the form '
        #self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
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
        #231: find the unpublished learning objective in the index

        elem = self.test_context.find_element_by_css_selector(".unpublished .edit .post-title")

        # Ensure element is visible
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        
        self.wait()

        elem.click()

        ' After opening edit Open Modal '

        #231: click the delete button
        elem = self.test_context.find_element_by_id("deleteButton")
        elem.click()

        ' Delete Item from Modal '        
        
        #231: then click the continue button
        elem = self.test_context.find_element_by_id("deleteModalContinueButton")
        elem.click()
        
        self.wait(s=2)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        
        items_after = self.test_context.find_elements_by_class_name("post-preview")
        
        #231: items after should be less than before
        
        self.assertEqual(4, len(items_after))
