from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_content_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        #self.test_context.implicitly_wait(10)
        
        # setup

        self.do_log_in(self.root_uri + "/schemesofwork/{}/curriculum-content/new".format(self.test_scheme_of_work_id))

        # create content
        
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-letter_prefix")
        elem.clear()
        elem.send_keys("A")

        elem = self.test_context.find_element_by_id("ctl-description")
        elem.send_keys("test page  redirect to index if valid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Curriculum/Course content')



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
        
        self.wait()

        ' After opening edit Open Modal '

        #231: click the delete button
        elem = self.test_context.find_element_by_id("deleteButton")
        elem.click()

        ' Delete Item from Modal '        
        
        #231: then click the continue button
        elem = self.test_context.find_element_by_id("deleteModalContinueButton")
        elem.click()
        
        self.wait(s=5)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Curriculum/Course content')
        
        items_after = self.test_context.find_elements_by_class_name("post-preview")
        
        #231: items after should be less than before
        
        self.assertEqual(9, len(items_after))
