from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_lesson_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):

        # setup
        #231: create a new resource
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/new", wait=1)
        
        # arrange
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # act

        ' Create valid information '

        ' ctl-year_id - select Yr12 VALID '
        elem = self.test_context.find_element_by_id("ctl-year_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Yr12":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-order_of_delivery_id '
        elem = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        elem.clear()
        elem.send_keys("1")

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys("Consectetur adipiscing elit")

        ' ctl-summary '
        elem = self.test_context.find_element_by_id("ctl-summary")
        elem.clear()
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-content_id - select following and writing algorithms '
        elem = self.test_context.find_element_by_id("ctl-content_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "following and writing algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-topic_id - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)
        
        ' ctl-key_words '
        '''
        elem = self.test_context.find_element_by_id("keywords-tokenfield")
        elem.send_keys("Comparison operator")
        elem.send_keys(Keys.TAB)
        elem.send_keys("AND")
        elem.send_keys(Keys.TAB)
        elem.send_keys("OR")
        elem.send_keys(Keys.TAB)
        elem.send_keys(Keys.TAB)
        '''

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)

        # assert
        ' should return to edit be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','Lessons')

        #231: items after should be less than before
        
        expected_item_per_page = [10,10,6,0]

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_redirect_to_index_after_deletion(self):

        #delete

        ' Open edit - go to page 1 '
        self.delete_unpublished_item(".unpublished a.edit .fa-edit", f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/?page=1")
        
        self.wait(s=2)

        # back to index

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
        
        #231: items after should be less than before

        expected_item_per_page = [10,10,5,0]

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()
