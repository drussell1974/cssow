from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_schemesofwork_index(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/schemesofwork/index")
        self.test_context.implicitly_wait(4)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/index')


    def test_page__navigate_to_learning_episode_index(self):

        # setup

        elem = self.test_context.find_element_by_id("lnk-schemeofwork-76")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

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


    def not_test_page__submenu__navigate_to_schemesofwork_new(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/schemesofwork/index")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/edit/new')





