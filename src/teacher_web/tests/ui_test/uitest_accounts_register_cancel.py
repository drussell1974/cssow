from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_register_cancel(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.test_path = "/accounts/register/"
        self.do_get(self.root_uri + self.test_path, wait=4)


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('', 'Account', 'Registration')
        #self.assertPageShouldHaveGroupHeading("")
        self.assertFooterContextText("")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)

    
    def test_page__should_redirect(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' ENTER SOMETHING BEFORE CANCELLING '
        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("test@localhost")


        elem = self.test_context.find_element_by_id("id_first_name")
        elem.clear()
        elem.send_keys("Mr D")

        ' cancel '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')
        #self.assertPageShouldHaveGroupHeading("")
