from datetime import datetime
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofwork_edit_existing(UITestCase):

    
    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/edit")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()
        

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'A-Level Computer Science')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        

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
        elem = self.test_context.find_element_by_id("saveDraftButton")
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
        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    ''' Test Save options - Default, Next, Add another '''

    def test_page__should_redirect_to_default_if_valid(self):
        ''' Test Save option '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '

        elem = self.find_wizardoptions_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__should_redirect_to_next_if_valid(self):
        ''' Test Next option '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        
        elem = self.find_wizardoptions_element_by_id("saveButtonNext")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new content for A-Level Computer Science')


    def test_page__should_redirect_to_add_another_if_valid(self):
        ''' Test Add another option '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        elem = self.find_wizardoptions_element_by_id("saveButtonAnother")
        
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Create new scheme of work')


    def test_page__should_redirect_to_skip_if_invalid(self):
        ''' Test Skip button - invalidate '''

        # setup
        elem = self.test_context.find_element_by_tag_name("form")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' Fill in field as blank '
        elem = self.test_context.find_element_by_id("ctl-name")
        elem.clear()
        self.wait(s=1)

        ' submit the form '
        elem = self.test_context.find_element_by_id("skipButton")
        elem.send_keys(Keys.RETURN)
        
        self.wait(s=2)
        
        # assert
        ' should be next page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new content for A-Level Computer Science')
