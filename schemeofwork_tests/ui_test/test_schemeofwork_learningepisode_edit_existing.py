from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepisode_edit_existing(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningepisode/edit?id={learning_episode_id}&scheme_of_work_id={scheme_of_work_id}&_next=%2Fschemeofwork%2Flearningepisode%2Findex%2F{scheme_of_work_id}".format(learning_episode_id=self.test_learning_episode_id, scheme_of_work_id=self.test_scheme_of_work_id))

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edits """

    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-order_of_delivery_id - 0 INVALID '
        elem = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        elem.clear()
        elem.send_keys(0)

        elem.send_keys(Keys.TAB)

        ' ctl-key_words '
        elem = self.test_context.find_element_by_id("ctl-key_words-tokenfield")
        elem.clear()
        elem.send_keys("algorithm")
        elem.send_keys(Keys.TAB)
        elem.send_keys("Ipsum")
        elem.send_keys(Keys.TAB)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Lesson', 'A-Level Computer Science Programming and development - Lesson 1')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem_form = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem_form)

        # test

        ' Create valid information '

        ' ctl-year_id - select Yr13 VALID '
        elem = self.test_context.find_element_by_id("ctl-year_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Yr13":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-order_of_delivery_id '
        elem_order_of_delivery_id = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        elem_order_of_delivery_id.clear()
        elem_order_of_delivery_id.send_keys("1")

        ' ctl-title '
        elem_title = self.test_context.find_element_by_id("ctl-title")
        elem_title.clear()
        elem_title.send_keys("Data Representation: Sound")

        ' ctl-topic_id - select KS4 '
        elem_topic_id = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem_topic_id.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()

        elem_topic_id.send_keys(Keys.TAB)

        ' ctl-summary '
        elem_summary = self.test_context.find_element_by_id("ctl-summary")
        elem_summary.clear()
        elem_summary.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-key_words SKIP adds too many '

        ' submit the form '
        elem_saveButton = self.test_context.find_element_by_id("saveButton")
        elem_saveButton.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Lessons', 'A-Level Computer Science')

