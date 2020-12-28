from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_content_edit_cancel(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        #231: open a learning objective
        self.do_log_in(self.root_uri + "/schemesofwork/{}/curriculum-content/{}/edit".format(self.test_scheme_of_work_id, self.test_content_id))
        # TODO: improve performance 
        self.wait()


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_stay_on_same_page_if_stay(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' Open Modal '

        #231: click the cancel button
        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()

        ' click no '        
        
        #231: then click the stay button
        elem = self.test_context.find_element_by_id("cancelModalStayButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Edit: data representation')


    def test_page__should_redirect_to_index_if_continue(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' Open Modal '

        #231: click the cancel button
        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()
        self.wait(s=2)
    
        ' click no (finding button appears to cancel dialog) '        
        
        #231: then click the continue button
        elem = self.test_context.find_element_by_id("cancelModalContinueButton")
        elem.click()
        # improve performance 
        self.wait()

        # assert
        ' should be redirected '
        self.assertWebPageTitleAndHeadings('', 'Log In', 'Register to create schemes of work and lessons')
