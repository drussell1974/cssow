from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_default(UITestCase):

    test_context = webdriver.Firefox()
    def setUp(self):
        # set up
        self.test_context.get("http://127.0.0.1:8000/schemeofwork/default/index")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings("schemeofwork", "Computing Schemes of work and lessons", "Computing schemes of work lessons across all key stages")









