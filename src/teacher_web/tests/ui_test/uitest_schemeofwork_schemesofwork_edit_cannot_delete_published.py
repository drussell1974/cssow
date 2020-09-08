from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_schemesofwork_edit_cannot_delete_published(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # setUp use existing
        #231 TODO: open an existing resource
        self.do_log_in(self.root_uri + "/schemesofwork/{}/edit".format(self.test_scheme_of_work_id))


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
        attr = elem.get_attribute("disabled")
        self.assertTrue(attr)

        #231: stay on page

        # check this does nothing (#290 commented out due to error Element <button id="deleteButton" class="btn btn-danger stackable float-right" name="published" type="submit"> is not clickable at point (945,845) because another element <li class="ui-menu-item"> obscures it)
        #elem.click()
        
        #231: assert we're still on the stay on page

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'A-Level Computer Science')
        