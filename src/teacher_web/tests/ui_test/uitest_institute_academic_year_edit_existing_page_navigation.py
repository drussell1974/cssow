from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_institute_academic_year_edit_existing_page_navigation(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/academic-years/2020/edit", wait=4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__breadcrumb__navigate_to_institute_index(self):
        #test
        elem = self.test_context.find_element_by_id('btn-bc-institute')
        self.assertEqual("Institute", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Institutes')
        

    def test_page__breadcrumb__navigate_to_academic_year_index(self):
        #test
        elem = self.test_context.find_element_by_id('btn-bc-academic_year')
        self.assertEqual("Academic Years", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Academic Years')