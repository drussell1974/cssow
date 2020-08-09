from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class test_schemeofwork_resources_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.test_context.implicitly_wait(20)
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/resources/new".format(self.test_scheme_of_work_id, self.test_lesson_id))


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

        ' ctl-title - leave EMPTY '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys(Keys.TAB)


        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','Types of CPU architecture','New')


    def test_page__markdownfile_type_stay_on_same_page_if_invalid(self):
        # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Website")

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' ctl-publisher '
        elem = self.test_context.find_element_by_id("ctl-publisher")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-uri '
        elem = self.test_context.find_element_by_id("ctl-uri")
        elem.clear() # Ensure filed is clear
                
        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','Types of CPU architecture','New')
        
        

    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Markdown")

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' ctl-notes '
        elem = self.test_context.find_element_by_id("ctl-notes")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mollis ligula dui, quis feugiat elit hendrerit condimentum. Mauris dignissim ultrices.")
        
        ' ctl-publisher '
        elem = self.test_context.find_element_by_id("ctl-publisher")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        #' ctl-uri '
        #elem = self.test_context.find_element_by_id("ctl-uri")
        #elem.send_keys("https://www.pgonline.co.uk/resources/computer-science/a-level-ocr/ocr-a-level-textbook/")

        ' ctl-md_document_name '
        elem = self.test_context.find_element_by_id("ctl-md_file")
        import os
        test_file = "{}/TEST.md".format(os.getcwd())
        elem.send_keys(test_file)

        ' submit the form '
        #self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')

        # open newly created resource to edit

        self.open_unpublished_item()

        # verify with preview that document is stored (required markdown-service running)

        self.wait(s=2)

        elem = self.test_context.find_element_by_css_selector("#md_document-preview--control > button#btn-markdown_preview")
        elem.click()

        self.assertEqual("PREVIEW MARKDOWN: TEST.MD", elem.text, "markdown document preview not found. Ensure service is running and available")


        elem = self.test_context.find_element_by_css_selector("#md_document-preview--control > .collapse > .markdown-body > h1")
        
        # THIS IS THE HEADING FROM THE LOADED MARKDOWN (THIS SHOULD BE THE FIRST ELEMENT OR BE INCLUDED... format should be hash for h1 - e.g. '#Donec fermentum')

        self.assertEqual("Donec fermentum", elem.text)


        ' After opening edit Open Modal '

        #231: click the delete button
        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()

        ' Cancel from Modal '        
        
        #231: then click the continue button
        elem = self.test_context.find_element_by_id("cancelModalContinueButton")
        elem.click()

        # delete

        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()


        


    def test_page__should_hide_upload_if_not_md_document_type(self):
        # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Website")

        # assert

        ' ctl-md_document_name '
        elem = self.test_context.find_element_by_id("md_document--control-group")
       
        self.assertFalse(elem.is_displayed(), "md_document_name--control should not be visible")


    def test_page__should_hide_upload_if_is_md_document_type(self):
        # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Markdown")

        # assert

        ' ctl-md_document_name '
        elem = self.test_context.find_element_by_id("md_document--control-group")
       
        self.assertTrue(elem.is_displayed(), "md_document_name--control should be visible")
