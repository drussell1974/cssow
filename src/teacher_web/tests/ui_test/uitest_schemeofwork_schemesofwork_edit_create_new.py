from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_schemesofwork_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + "/schemesofwork/new")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'New')
        
        save = self.test_context.find_element_by_id('saveButton')
        self.assertEqual("DRAFT", save.text)

        saveandpublish = self.test_context.find_element_by_id('saveAndPublishButton')
        self.assertEqual("SAVE AND PUBLISH", saveandpublish.text)


    def test_page__breadcrumb_navigate_to_lesson_index_not_visible_for_new_schemeofwork(self):
        # test and assert
        with self.assertRaises(Exception):
            self.test_context.find_element_by_id('btn-bc-lessons')


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
        elem = self.test_context.find_element_by_name("edit-schemeofwork")

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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'New')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-description")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' name '
        elem = self.test_context.find_element_by_id("ctl-name")
        elem.send_keys("should_redirect_to_index_if_valid")

        ' exam board - just skip as not required'
        elem = self.test_context.find_element_by_id("ctl-exam_board_id")
        elem.send_keys(Keys.TAB)

        ' key stage - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-key_stage_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "KS4":
                 opt.click()

        elem.send_keys(Keys.TAB)

        ' description - Fill in field with some information '
        elem.send_keys("test_schemeofwork_schemesofwork_new.test_page__edit_existing__should_redirect_to_index_if_valid, last updated this field {}" + str(datetime.now()))

        ' select the submit button (to remove cursor from textarea '

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=1)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')

        #delete
        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()


