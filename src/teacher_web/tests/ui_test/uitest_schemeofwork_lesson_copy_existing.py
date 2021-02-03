from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lesson_copy_existing(UITestCase):
   
    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in('/schemesofwork/{}/lessons/{}/copy'.format(self.test_scheme_of_work_id, self.test_lesson_id))

        self.wait(s=2)

    def tearDown(self):
        # tear down
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have_correct_elements(self):

        ' ensure headings are correct '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','Create new lesson for A-Level Computer Science', 'TEST USER')
    
        ' year group dropdown ' 
        elem = self.test_context.find_elements_by_xpath(".//*[@id='ctl-year_id']/option")
        self.assertEqual(3, len(elem))
        elem = Select(self.test_context.find_element_by_id("ctl-year_id"))
        selected_option = elem.first_selected_option
        self.assertEqual("Yr12", selected_option.text)

        ' order of delivery - ctl-order_of_delivery_id' 
        elem = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        self.assertEqual("3", elem.get_attribute("value"))
        
        ' title '
        elem = self.test_context.find_element_by_id("ctl-title")
        self.assertEqual("copy of Types of CPU architecture", elem.get_attribute("value"))
        
        ' summary ' 
        elem = self.test_context.find_element_by_id("ctl-summary")
        self.assertEqual("Von Neumann architecture and Harvard architecture, and CISC and RISC", elem.get_attribute("value"))

        ' topic dropdown '
        elem = self.test_context.find_elements_by_xpath(".//*[@id='ctl-topic_id']/option")
        self.assertEqual(7, len(elem))
        elem = Select(self.test_context.find_element_by_id("ctl-topic_id"))
        selected_option = elem.first_selected_option
        self.assertEqual("Algorithms", selected_option.text)


    """ Test edits """
    def test_page__should_stay_on_same_page_if_invalid(self):
          
        # arrange 
        elem = self.test_context.find_element_by_tag_name("form")
        
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-title - select EMPTY '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys("")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','Create new lesson for A-Level Computer Science')
        

    def test_page__should_redirect_to_index_if_valid(self):

        # arrange 
        elem = self.test_context.find_element_by_tag_name("form")

        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-title - select EMPTY '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys("COPY test_page__should_redirect_to_index_if_valid")


        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        # TODO: improve performance
        self.wait()
        
        # assert
        ' should return to edit be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','Lessons')
    
        # delete

        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()
        