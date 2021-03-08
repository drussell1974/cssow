from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from tests.test_helpers.decorators import restore_demo_data

class uitest_schemeofwork_schemesofworkkeyword_edit_cancel(UITestCase):

    test_context = WebBrowserContext()

    @restore_demo_data()
    def setUp(self):
        #231: TODO: open existing resource
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/{self.test_keyword_id}/edit", wait=2)


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

        elem = self.find_element_by_id__with_explicit_wait("cancelButton")
        elem.click()

        ' click no '        
        
        elem = self.find_element_by_id__with_explicit_wait("cancelModalStayButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Edit keyword: Random Access Memory (RAM) for Computing curriculum for A-Level')


    def test_page__should_redirect_to_index_if_continue(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' Open Modal '

        elem = self.find_element_by_id__with_explicit_wait("cancelButton", wait=5)
        elem.click()


        ' click no (finding button appears to cancel dialog) '        
        
        elem = self.find_element_by_id__with_explicit_wait("cancelModalContinueButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should be redirected '
        self.assertWebPageTitleAndHeadings('', 'Log in', 'Register to create schemes of work and lessons')
