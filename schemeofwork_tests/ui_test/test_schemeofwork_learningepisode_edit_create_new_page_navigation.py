from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningepisode_edit_create_new_page_navigation(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningepisode/edit?scheme_of_work_id={}".format(self.test_scheme_of_work_id))


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
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Episode', 'for A-Level Computer Science')


    """ Breadcrumb """


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("schemes of work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes Of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_learningepisode_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_episodes')
        self.assertEqual("episodes", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Episodes', 'for A-Level Computer Science') # needs to show scheme of work


    def test_page__breadcrumb__navigate_to_learningobjective_index__should_not_show_on_page_for_new_item(self):
        #test

        with self.assertRaises(Exception):
            self.test_context.find_element_by_id('btn-new')

