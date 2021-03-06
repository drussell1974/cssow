#from unittest import TestCase
import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

TEST_USER_NAME = os.environ["TEST_USER_NAME"]
TEST_USER_PSWD = os.environ["TEST_USER_PSWD"]

def WebBrowserContext(restore_demo_data=False):
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    webdriver.Chrome(chrome_options=options)
    # browser.implicitly_wait(5)
    if restore_demo_data:
        print("restoring demo data...", end="")
        uri = os.environ["TEST_URI"] + "/api/demo/restore-data"
        print(uri, end="")
        webdriver.get(uri)

        print("...restored demo data!")

    return webdriver


class UITestCase(TestCase):
    root_uri = "http://localhost:8000/"
    test_scheme_of_work_id = 11
    test_lesson_id = 131
    test_learning_objective_id = 410
    test_reference = 983
    test_keyword_id = 92

    def wait(self, s=3):
        time.sleep(s)


    def assertWebPageFooter(self, institute_name, department_name):

        # test - institute name
        self.assertEqual(institute_name, self.test_context.find_element_by_id("footer_institute-name").text)
        # test - department name
        self.assertEqual(department_name, self.test_context.find_element_by_id("footer_department-name").text)


    def assertWebPageTitleAndHeadings(self, title, h1, subheading):

        # test - subheading
        self.assertEqual(title, self.test_context.title, "title not as expected")
        # assert - site-heading
        self.assertEqual(h1, self.test_context.find_element_by_tag_name("h1").text)
        # assert - title
        self.assertEqual(subheading, self.test_context.find_element_by_class_name("subheading").text)


    def try_log_in(self, redirect_to_uri_on_login, enter_username="test@localhost", enter_password="password1.", wait=0):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """

        ' Open uri - if authentication is required this should automatically redirect to login '
        self.do_get(redirect_to_uri_on_login, wait=wait)
        #self.test_context.implicitly_wait(wait)

        try:

            elem = self.test_context.find_element_by_id("auth_user_email")
            elem.send_keys(enter_username)
            #elem.send_keys(Keys.TAB)

            elem = self.test_context.find_element_by_id("auth_user_password")
            elem.send_keys(enter_password)

            ' submit the form '
            elem.send_keys(Keys.RETURN)


        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            pass


    def do_log_in(self, redirect_to_uri_on_login, wait=1, enter_username="test@localhost", enter_password="password1."):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """
        login_uri = "http://dev.computersciencesow.net:8000/schemeofwork/default/user/login"

        ' Open uri - if authentication is required this should automatically redirect to login '
        
        go_to_url = "{}?_next={}".format(login_uri, redirect_to_uri_on_login)
        
        self.test_context.get(go_to_url)
        #self.test_context.implicitly_wait(wait)
        
        try:
            elem = self.test_context.find_element_by_id("auth_user_email")
            elem.send_keys(enter_username if None else TEST_USER_NAME)
            
            elem = self.test_context.find_element_by_id("auth_user_password")
            elem.send_keys(enter_password if None else TEST_USER_PSWD)

            ' submit the form '
            elem.send_keys(Keys.RETURN)

            if wait > 0:
                self.wait(s=wait)
                
        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            #print('try_log_in handled - already logged in (probably) - {}'.format(e.args))
            pass
