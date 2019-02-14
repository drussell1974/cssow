from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepisode_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningepisode/edit?scheme_of_work_id=11")

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-key_stage_id - select EMPTY '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "- Select an option for topic -":
                 opt.click()

        elem.send_keys(Keys.TAB)


        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Lesson','A-Level Computer Science - Lesson 1')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

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
        elem.send_keys("Data Representation: Sound")

        ' ctl-summary '
        elem = self.test_context.find_element_by_id("ctl-summary")
        elem.clear()
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-key_words '
        elem = self.test_context.find_element_by_id("ctl-key_words-tokenfield")
        elem.clear()
        elem.send_keys("Algorithm")
        elem.send_keys(Keys.TAB)
        elem.send_keys("Ipsum")
        elem.send_keys(Keys.TAB)



        ' ctl-topic_id - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' div-pathway_objective_id  - select VALID '
        # expand accordion
        self.test_context.implicitly_wait(4) # wait for accordion to load from ajax call
        elem = self.test_context.find_element_by_id('ks3-heading-text')
        elem.click()

        elem = self.test_context.find_element_by_id('ctl-pathway_objective_id477')
        elem.click()
        elem.send_keys(Keys.TAB)
        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Learning objectives','Data Representation: Sound')
