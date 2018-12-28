from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningobjective_edit_create_new_page_navigation(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/learningobjective/edit?learning_episode_id={}&scheme_of_work_id={}".format(self.test_learning_episode_id, self.test_scheme_of_work_id))


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
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning objective', 'for A-Level Computer Science - Week 1 - Algorithms')


    """ Breadcrumb """


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("Schemes of work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes of work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_learningepisode_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_episodes')
        self.assertEqual("Episodes", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episodes', 'for A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_learningobjective_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_objectives')
        self.assertEqual("Objectives", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning objectives', 'for A-Level Computer Science - Week 1 - Algorithms')
