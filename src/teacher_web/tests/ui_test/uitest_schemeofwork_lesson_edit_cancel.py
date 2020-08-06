from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_lesson_edit_cancel(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.test_context.implicitly_wait(10)
        #231: TODO: open existing resource
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/edit".format(self.test_scheme_of_work_id, self.test_lesson_id))


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
        elem.click()

        ' click no '        
        
        elem = self.test_context.find_element_by_id("cancelModalStayButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Edit: Types of CPU architecture')


    def test_page__should_redirect_to_index_if_continue(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' Open Modal '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()


        ' click no (finding button appears to cancel dialog) '        
        
        elem = self.test_context.find_element_by_id("cancelModalContinueButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should be redirected '
        self.assertWebPageTitleAndHeadings('', 'Log In', 'Register to create schemes of work and lessons')
