from datetime import datetime
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofwork_edit_existing(UITestCase):

    
    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + "/schemesofwork/{}/edit".format(self.test_scheme_of_work_id))


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'A-Level Computer Science')
        
        save = self.test_context.find_element_by_id('saveButton')
        self.assertEqual("DRAFT", save.text)

        saveandpublish = self.test_context.find_element_by_id('saveAndPublishButton')
        self.assertEqual("SAVE AND PUBLISH", saveandpublish.text)


    def test_page__breadcrumb_navigate_to_lesson_index(self):
        # test
        
        elem = self.test_context.find_element_by_id('btn-bc-lessons')
        self.assertEqual("Lessons", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # test
        elem = self.test_context.find_element_by_id('btn-bc-schemes_of_work')
        self.assertEqual("Schemes of Work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    """ edit """


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Fill in field as blank '
        elem = self.test_context.find_element_by_id("ctl-name")

        elem.clear()
        elem.send_keys("")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'A-Level Computer Science')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveAndPublishButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=1)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')