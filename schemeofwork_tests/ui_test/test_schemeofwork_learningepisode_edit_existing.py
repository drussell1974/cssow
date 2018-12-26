from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningepisode_edit_existing(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/learningepisode/edit?id=47&scheme_of_work_id=76")


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
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episode', 'for Selenium UI Test')


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
        self.assertEqual("Episodes", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/index/76')


    def test_page__breadcrumb__navigate_to_learningobjective_index(self):
        #test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[4]/a')
        self.assertEqual("Objectives", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('learningobjective/index/47/76')


    """ Test edits """

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
        time.sleep(3)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/edit/47/76')


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

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadingsByRoute('learningobjective/index/47/76')

