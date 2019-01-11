from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/learningepisode/index/{}".format(self.test_scheme_of_work_id))
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
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episodes', 'for A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes of work', 'Our shared schemes of work by key stage')


    def test_page__submenu__navigate_to_learningepisode_new(self):
        # setup
        self.do_log_in("/schemeofwork/learningepisode/index/{}".format(self.test_scheme_of_work_id))

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episode', 'for A-Level Computer Science')



