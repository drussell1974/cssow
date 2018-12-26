from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningepisode_create_new(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/learningepisode/edit&scheme_of_work_id=76")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    """ Test content """

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episode', 'for')


    """ Breadcrumb """

    def test_page__breadcrumb__navigate_to_default_index(self):
        #test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[1]/a')
        self.assertEqual("Home", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('default/index')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[2]/a')
        self.assertEqual("Schemes of work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/index')


    def test_page__breadcrumb__navigate_to_learningepisode_index(self):
        #test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[3]/a')
        #self.assertEqual("Episodes", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episodes', 'for') # needs to show scheme of work


    def test_page__breadcrumb__navigate_to_learningobjective_index__should_not_show_on_page_for_new_item(self):
        #test

        with self.assertRaises(Exception):
            self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[4]/a')



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

        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        ' sleep to give time to ensure browser HAS not redirected '
        import time
        time.sleep(1)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Learning episode','for')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-order_of_delivery_id '
        elem = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        elem.clear()
        elem.send_keys("1")

        ' ctl-key_stage_id - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()

        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        ' sleep to give time to ensure browser HAS not redirected '
        import time
        time.sleep(1)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Learning episode','for')
