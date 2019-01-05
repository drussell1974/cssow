from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_default_index(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/default/index")
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
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Computing Schemes of work and lessons', 'Computing schemes of work lessons across all key stages')


    def test_page__navigate_to_all_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('btn-all-schemes-of-work').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes of work', 'Our shared schemes of work by key stage')









