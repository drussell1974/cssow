from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_schemesofwork_edit_cancel(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/edit")

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

        elem = self.test_context.find_element_by_id("cancelButton")
        self.wait(s=1)
        elem.click()
        
        ' click no '        
        
        elem = self.test_context.find_element_by_id("cancelModalStayButton")
        self.wait(s=1)
        elem.click()
        
        self.wait()

        # assert
        ' should still be on the same page '
        #231: assert we're still on the same page
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Computer Science', 'A-Level Computer Science')


    def test_page__should_redirect_to_index_if_continue(self):
        # setup

        ' Open Modal '

        elem = self.find_element_by_id__with_explicit_wait("cancelButton")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)
        elem.click()

        ' click yes, cancel (finding button appears to cancel dialog) '        
        
        elem = self.find_element_by_id__with_explicit_wait("cancelModalContinueButton")
        elem.click()

        # assert
        ' should be redirected '
        self.assertWebPageTitleAndHeadings('', 'Log in', 'Register to create schemes of work and lessons')
