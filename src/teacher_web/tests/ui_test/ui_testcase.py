import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def WebBrowserContext():

    ''' Uncomment Chrome driver -- chromedriver.exe '''
    #options = webdriver.ChromeOptions()
    #options.add_argument("--start-maximized")
    #return webdriver.Chrome()

    ''' Uncomment for Firefox -- geckodriver.exe '''
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    browser = webdriver.Firefox(firefox_options=fireFoxOptions)
    
    return browser


TEST_USER_NAME = os.environ["TEST_USER_NAME"]
TEST_USER_PSWD = os.environ["TEST_USER_PSWD"]

class UITestCase(TestCase):                                                                     
    root_uri = os.environ["TEST_URI"]

    test_institute_id = os.environ["TEST_INSTITUTE_ID"]
    test_department_id = os.environ["TEST_DEPARTMENT_ID"]
    test_scheme_of_work_id = os.environ["TEST_SCHEME_OF_WORK_ID"]
    test_content_id = os.environ["TEST_CONTENT_ID"]
    test_lesson_id = os.environ["TEST_LESSON_ID"] 
    test_learning_objective_id = os.environ["TEST_LEARNING_OBJECTIVE_ID"]
    test_reference = os.environ["TEST_RESOURCE_ID"]
    test_md_document_name = os.environ["TEST_MD_DOCUMENT_NAME"]
    test_keyword_id = os.environ["TEST_KEYWORD_ID"]
    TEST_KEYWORD_TERM = os.environ["TEST_KEYWORD_TERM"]
    TEST_KEYWORD_RENAME_TERM_TO = os.environ["TEST_KEYWORD_RENAME_TERM_TO"]
    
    def wait(self, s = 3):
        time.sleep(s)

    def do_get(self, uri, wait=0):
        self.test_context.get(uri)
        self.test_context.implicitly_wait(wait)

    def find_element_by_id__with_explicit_wait(self, element_id, wait=2):
        # TODO: scroll element into view - check functionality
        #self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem = WebDriverWait(self.test_context, wait).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        return elem


    def assertSidebarResponsiveMenu(self, section_no, expected_title, expected_no_of_items):
        
        # title
        title_elem = self.test_context.find_element_by_xpath('//*[@id="sidebarResponsive"]/div/section[{}]/div/div[1]/h5'.format(section_no))

        # list lists
        list_item_elems = self.test_context.find_elements_by_xpath('//*[@id="sidebarResponsive"]/div/section[{}]/div/div[2]/ul/li'.format(section_no)) 

        # assert
        self.assertEqual(expected_title, title_elem.text)
        self.assertGreaterEqual(len(list_item_elems), expected_no_of_items, "number of items not as expected")


    def assertFooterContextText(self, context_text):
        # assert - context_text
        self.assertEqual(context_text, self.test_context.find_element_by_id("footer-context--text").text, f"#footer-context--text not as expected.")
        

    def assertWebPageTitleAndHeadings(self, title, h1, subheading, should_be_logged_in=None, username=None, failed_message = "assertWebPageTitleAndHeadings failed", wait=0):

        # test - subheading
        self.assertEqual(subheading, self.find_element_by_id__with_explicit_wait("main-subheading", wait=wait).text, f".subheading not as expected ({failed_message})")
        # assert - site-heading
        self.assertEqual(h1, self.test_context.find_element_by_tag_name("h1").text, f".main_heading not as expected ({failed_message})")
        # assert - title
        self.assertEqual(title, self.test_context.title, f"title not as expected ({failed_message})")
        
        
        # assert - username
        if should_be_logged_in == True and username != None:
            profile = self.test_context.find_element_by_id("btn-profile")
            self.assertEqual(username.upper(), profile.text.upper(), f"#btn-profile (username button) not as expected ({failed_message})")
        elif should_be_logged_in == False:
            profile = self.test_context.find_element_by_id("btn-login")
            self.assertEqual("Login", profile.text, f"#btn-login (Login button) text not as expected ({failed_message})")


    def assertCustom404(self, info_message):
        elem = self.test_context.find_element_by_css_selector('#info > p')
        self.assertEqual(info_message, elem.text)


    def assertCustomPermissionDenied(self, h1):
        elem = self.test_context.find_element_by_css_selector("div#summary h1")
        self.assertEqual(h1, elem.text)


    def assertLoginPage(self, redirect_to_url="", login_message = "", exception_message="", failed_message = "assertLoginPage failed"):
        elem = self.test_context.find_element_by_css_selector("div.site-heading > h1")
        self.assertEqual("Log in", elem.text, f"text for element .site-heading h1 at '{redirect_to_url}' not expected - {failed_message}")
        # TODO: #206 assert messages
        elem = self.test_context.find_element_by_id("login_message")
        self.assertEqual(login_message, elem.text, f"text for element #login_message at '{redirect_to_url}' not expected  - {failed_message}")


    def try_log_in(self, redirect_to_uri_on_login, enter_username=None, enter_password=None, wait=1):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """
        
        ' Open uri - if authentication is required this should automatically redirect to login '
        self.do_get(redirect_to_uri_on_login, wait=wait)

        try:

            elem = self.find_element_by_id__with_explicit_wait("id_username")
            elem.send_keys(enter_username if None else TEST_USER_NAME)
            
            elem = self.test_context.find_element_by_id("id_password")
            elem.send_keys(enter_password if None else TEST_USER_PSWD)

            ' submit the form '
            elem.send_keys(Keys.RETURN)

        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            pass


    def try_click_log_out(self, wait):
        try:
            elem = self.find_element_by_id__with_explicit_wait("btn-logout", wait)    
            elem.click()
        except Exception as e:
            #print("try_click_log_out handled - probably logged out already ({})".format(e.args))
            pass # ignore errors as may already be logged out


    def try_log_out(self, uri, wait=1):
        
        self.try_click_log_out(wait=wait)

        self.test_context.get(self.root_uri + uri)
        
        self.test_context.implicitly_wait(wait)  # reinstate

    
    def do_log_in(self, redirect_to_uri_on_login, wait=4, enter_username=None, enter_password=None):
        """
        Makes an attempt to log in, if the page has been redirected.
        If the inputs for login are not found, then this is handled; it assumes the user is already logged in
        """
        #print(f"do_log_in: {redirect_to_uri_on_login}")
        enter_username = enter_username if enter_username is not None else TEST_USER_NAME
        enter_password = enter_password if enter_password is not None else TEST_USER_PSWD

        ' Try log out first '

        self.try_click_log_out(wait=wait)
        
        ' Open uri - if authentication is required this should automatically redirect to login '

        login_uri = self.root_uri + "/accounts/login"
        self.test_context.get("{}?next={}".format(login_uri, redirect_to_uri_on_login))
        self.test_context.implicitly_wait(wait) # reinstate

        try:

            elem = self.find_element_by_id__with_explicit_wait("id_username")
            elem.send_keys(enter_username)
            
            elem = self.test_context.find_element_by_id("id_password")
            elem.send_keys(enter_password)

            ' submit the form '
            elem.send_keys(Keys.RETURN)

            if wait > 0:
                self.wait(s=wait)
            
        except Exception as e:
            ' if elements are not found then this will handle the exception assuming user is already logged in '
            print('try_log_in handled - already logged in (probably) - {}'.format(e.args))
            pass


    def open_unpublished_item(self, class_selector, page_url = None):

        if page_url is not None:
            self.do_log_in(self.root_uri + page_url)

        #231: find the unpublished item in the index

        elem = self.test_context.find_element_by_css_selector(class_selector)
        
        # Ensure element is visible
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)
        elem.click()
        

    def delete_unpublished_item(self, class_selector, page_url = None):
        """ open and delete unpublished item"""

        ' Open to edit '
        self.open_unpublished_item(class_selector, page_url)

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


    def run_testcases__permission(self, testcases, batch_name):

        #print(f"running {len(testcases)} test cases for {batch_name}!", end="")

        for testcase in testcases:
            try:
            
                # test
                if "skip" in testcase.keys() and testcase["skip"] == True:
                    print("s", end="")
                else:
                    self.do_log_in(testcase["uri"], enter_username=testcase["enter_username"], wait=2)
                    
                    # assert
                    if testcase["allow"] == False:
                        self.assertLoginPage(login_message=testcase["exp__login_message"], redirect_to_url=testcase["uri"], exception_message="PermissionError at", failed_message=f"testcase {testcase['route']} failed.")
                    else:
                        self.assertWebPageTitleAndHeadings(testcase["exp__title"], testcase["exp__h1"], testcase["exp__subheading"], failed_message=f"testcase {testcase['route']} failed.")
            except KeyError as e:
                raise AssertionError(f"An error occurred running uri {testcase['uri']} for user {testcase['enter_username']} in test cases for {batch_name}! ensure correct keys have been provided", e)
            except Exception as e:
                raise AssertionError(f"An error occurred running {testcase} test cases for {batch_name}! ensure correct keys have been provided", e)
