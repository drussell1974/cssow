from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_register_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.try_log_in(self.root_uri + "/accounts/register")


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


    @skip("don't create new user during testing")
    def test_page__should_direct_to_confirmation_sent(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' first name '
        elem = self.test_context.find_element_by_id("id_username")
        elem.clear()
        elem.send_keys("test@localhost")

        ' enter password '
        elem = self.test_context.find_element_by_id("id_password1")
        elem.clear()
        elem.send_keys("password1.")

        ' confirm password '
        elem = self.test_context.find_element_by_id("id_password2")
        elem.clear()
        elem.send_keys("password1.")

        ' submit '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_elements_by_xpath("/html/body/div/div/div[3]/div/h1")
        self.assertEqual("Password changed", elem[0].text)

        self.assertWebPageTitleAndHeadings('', 'Account', 'Password changed')
        self.assertPageShouldHaveGroupHeading("")


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("test@localhost")



        elem = self.test_context.find_element_by_id("id_first_name")
        elem.clear()
        elem.send_keys("Mr R")


        elem = self.test_context.find_element_by_id("id_password1")
        elem.clear()

        elem = self.test_context.find_element_by_id("id_password2")
        elem.clear()

        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()

        self.wait(s=1)

        # assert

        elem = self.test_context.find_element_by_css_selector(".maincontent h1")
        self.assertEqual("Registration", elem.text)

        self.assertWebPageTitleAndHeadings('', 'Account', 'Registration')
        #self.assertPageShouldHaveGroupHeading("")

