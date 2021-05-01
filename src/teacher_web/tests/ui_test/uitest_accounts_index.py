from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/accounts/", wait=4)
        
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Test User', 'Your profile')
        self.assertFooterContextText("")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


    def test_page__card__navigate_to_change_password(self):
        # arrange
        
        # act
        self.test_context.find_element_by_id('btn-password_change--content').click()

        # assert
        self.assertWebPageTitleAndHeadings('', 'Account', 'Change password')


    def test_page__card__navigate_to_delete_account(self):
        # arrange
        
        # act
        self.test_context.find_element_by_id('btn-delete_account--content').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Account', 'Delete account')

