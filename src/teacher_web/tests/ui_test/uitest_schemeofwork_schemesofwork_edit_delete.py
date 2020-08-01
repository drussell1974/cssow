from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_schemesofwork_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):

        #self.test_context.implicitly_wait(10)
        # setup
        #231: create a new resource
        self.do_log_in(self.root_uri + "/schemesofwork/new")

        
        # setup
        elem = self.test_context.find_element_by_id("ctl-description")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' name '
        elem = self.test_context.find_element_by_id("ctl-name")
        elem.send_keys("should_redirect_to_index_if_valid")

        ' exam board - just skip as not required'
        elem = self.test_context.find_element_by_id("ctl-exam_board_id")
        elem.send_keys(Keys.TAB)

        ' key stage - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-key_stage_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "KS4":
                 opt.click()

        elem.send_keys(Keys.TAB)

        ' name '
        elem = self.test_context.find_element_by_id("ctl-description")
        ' description - Fill in field with some information '
        elem.send_keys("test_schemeofwork_schemesofwork_new.test_page__edit_existing__should_redirect_to_index_if_valid, last updated this field")

        ' select the submit button (to remove cursor from textarea '

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


        #TODO: #231: items after should be less than before
        
        items_before = self.test_context.find_elements_by_class_name("post-preview")
        self.assertEqual(4, len(items_before))


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

        # back to index

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', "Schemes of Work", 'Our shared schemes of work by key stage')
        
        #TODO: #231: items after should be less than before
        
        items_after = self.test_context.find_elements_by_class_name("post-preview")
        self.assertEqual(3, len(items_after))
