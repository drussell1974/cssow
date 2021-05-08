from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_accounts_register_join(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        self.try_log_in(self.root_uri + "/accounts/join")


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
        self.assertWebPageTitleAndHeadings('', 'Account', 'Complete registration')
        #self.assertPageShouldHaveGroupHeading("")
        self.assertFooterContextText("")
        self.assertTopNavShouldHaveHomeIndex(True)


    def test_page__should_create_login(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' email '
        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("join@localhost")

        ' first name '
        elem = self.test_context.find_element_by_id("id_first_name")
        elem.clear()
        elem.send_keys("You can delete me")

        ' join code '
        elem = self.test_context.find_element_by_id("id_join_code")
        elem.clear()
        elem.send_keys("ABCDEF")

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

        self.wait(s=4)

        self.do_log_in("/accounts/profile/", wait=4, enter_username="join@localhost", enter_password="password1.")

        # assert

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'You can delete me', 'Your profile')

        # tearDown

        elem = self.test_context.find_element_by_id("btn-delete_account--content")
        elem.click()
        self.wait(s=4)
        #' confirm delete ' 
        elem = self.test_context.find_element_by_id("deleteCheck")
        elem.click()
        #' delete ' 
        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        elem = self.test_context.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys("test@localhost")
        
        ''' invalidate '''
        elem = self.test_context.find_element_by_id("id_first_name")
        elem.clear() 

        elem = self.test_context.find_element_by_id("id_password1")
        elem.clear()

        elem = self.test_context.find_element_by_id("id_password2")
        elem.clear()

        elem = self.test_context.find_element_by_id("saveButton")
        elem.click()

        self.wait(s=1)

        # assert

        self.assertWebPageTitleAndHeadings('', 'Account', 'Complete registration')
        #self.assertPageShouldHaveGroupHeading("")

