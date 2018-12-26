from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/learningepisode/index?scheme_of_work_id=76")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/index/76')


    def test_page__breadcrumb__navigate_to_default_index(self):
        # setup
        self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[1]/a').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('default/index')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[2]/a').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/index')


    def test_page__submenu__navigate_to_learningepisode_new(self):
        # setup
        self.do_log_in("/schemeofwork/learningepisode/index?scheme_of_work_id=76")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/edit/new')



