from django.db import connection as db
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def WebBrowserContext():
    #options = webdriver.ChromeOptions()
    #options.add_argument("--start-maximized")
    return webdriver.Firefox()

TEST_USER_NAME = os.environ["TEST_USER_NAME"]
TEST_USER_PSWD = os.environ["TEST_USER_PSWD"]

class UITestCase(TestCase):
    root_uri = os.environ["TEST_URI"]
    test_scheme_of_work_id = os.environ["TEST_SCHEME_OF_WORK_ID"]
    test_content_id = os.environ["TEST_CONTENT_ID"]
    test_lesson_id = os.environ["TEST_LESSON_ID"] 
    test_learning_objective_id = os.environ["TEST_LEARNING_OBJECTIVE_ID"]
    test_reference = os.environ["TEST_RESOURCE_ID"]
    test_md_document_name = os.environ["TEST_MD_DOCUMENT_NAME"]

    def wait(self, s = 5):
        import time
        time.sleep(s)
    

    def assertWebPageTitleAndHeadings(self, title, h1, subheading, username=None):

        # test - subheading
        self.assertEqual(title, self.test_context.title, "title not as expected")
        # assert - site-heading
        self.assertEqual(h1, self.test_context.find_element_by_tag_name("h1").text)
        # assert - title
        self.assertEqual(subheading, self.test_context.find_element_by_class_name("subheading").text)
        # assert - username
        if username != None:
            profile = self.test_context.find_element_by_id("btn-profile")
            self.assertEqual(username, profile.text)


    def assertCustom404(self, info_message):
        elem = self.test_context.find_element_by_css_selector('#info > p')
        self.assertEqual(info_message, elem.text)


    def try_log_in(self, redirect_to_uri_on_login):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """

        ' Open uri - if authentication is required this should automatically redirect to login '
        self.test_context.get(redirect_to_uri_on_login)

        try:
            self.test_context.implicitly_wait(4)

            elem = self.test_context.find_element_by_id("id_username")
            elem.send_keys(TEST_USER_NAME)
            
            elem = self.test_context.find_element_by_id("id_password")
            elem.send_keys(TEST_USER_PSWD)

            ' submit the form '
            elem.send_keys(Keys.RETURN)


        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            pass


    def do_log_in(self, redirect_to_uri_on_login):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """
        
        login_uri = self.root_uri + "/accounts/login"

        ' Open uri - if authentication is required this should automatically redirect to login '
        self.test_context.get("{}?next={}".format(login_uri, redirect_to_uri_on_login))

        
        try:
            self.test_context.implicitly_wait(4)

            elem = self.test_context.find_element_by_id("id_username")
            elem.send_keys(TEST_USER_NAME)
            
            elem = self.test_context.find_element_by_id("id_password")
            elem.send_keys(TEST_USER_PSWD)
            ' submit the form '
            elem.send_keys(Keys.RETURN)
            self.wait(s=1)
            
        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            print('try_login handled - already logged in (probably) - {}'.format(e.args))
            pass



    def open_unpublished_item(self):
        #231: find the unpublished item in the index

        elem = self.test_context.find_element_by_css_selector(".unpublished .edit .post-title")

        # Ensure element is visible
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()
        

    def delete_unpublished_item(self):
        """ open and delete unpublished item"""

        ' Open to edit '
        self.open_unpublished_item()

        self.wait()

        ' After opening edit Open Modal '

        #231: click the delete button
        elem = self.test_context.find_element_by_id("deleteButton")
        elem.click()

        ' Delete Item from Modal '        

        #238: agree to delete item
        elem = self.test_context.find_element_by_id("deleteModalIAgree")
        elem.click()

        #231: then click the continue button
        elem = self.test_context.find_element_by_id("deleteModalContinueButton")
        elem.click()
