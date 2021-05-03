from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/accounts/delete", wait=4)
        
        self.wait(s=2)

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'test@localhost', 'Account')
        self.assertFooterContextText("")
        self.assertTopNavShouldHaveHomeIndex(True)
        #self.assertPageShouldHaveGroupHeading("Delete account")
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


    def test_page__has_confirmation_and_delete(self):
        # arrange
        
        # act

        # assert
        elem = self.test_context.find_element_by_id('deleteCheck')
        self.assertEqual("on", elem.get_attribute("value"))

        elem = self.test_context.find_element_by_id('deleteCheckLabel')
        self.assertEqual("I understand that my information will be permanently deleted", elem.text)

        elem = self.test_context.find_element_by_id('saveButton')
        self.assertEqual("Continue", elem.get_attribute("value"))

