from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_resources_edit_delete__cancel(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # setUp use existing
        #231 TODO: open an existing resource
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/resources/{}/edit".format(self.test_scheme_of_work_id, self.test_lesson_id, self.test_reference))


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_stay_on_page_after_cancelling_delete(self):

        #delete

        ' Open edit '

        elem = self.test_context.find_element_by_tag_name("form")

        # Ensure element is visible
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        
        elem.click()

        ' Open Modal '
        #231: click the delete button
        elem = self.test_context.find_element_by_id("deleteButton")
        elem.click()

        ' Delete Item from Modal '        
        #231: then click the stay button

        elem = self.test_context.find_element_by_id("deleteModalStayButton")
        elem.click()
        
        #231: assert we're still on the stay on page

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Edit: OCR AS and A Level Computer Science')
        