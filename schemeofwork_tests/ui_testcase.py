from unittest import TestCase
from selenium.webdriver.common.keys import Keys

class UITestCase(TestCase):
        test_scheme_of_work_id = 11
        test_learning_episode_id = 35
        test_learning_objective_id = 410

        root_uri = "http://dev.computersciencesow.net:8000/schemeofwork/"


        def wait(self):
            import time
            time.sleep(5)

        def assertWebPageTitleAndHeadings(self, title, h1, subheading):

            # test - subheading
            self.assertEqual(title, self.test_context.title, "title not as expected")
            # assert - site-heading
            self.assertEqual(h1, self.test_context.find_element_by_tag_name("h1").text)
            # assert - title
            self.assertEqual(subheading.lower(), self.test_context.find_element_by_class_name("subheading").text)


        def try_log_in(self, redirect_to_uri_on_login):
            """
            Makes an attempt to log in, if the page has been redirected.
            If the inputs for login are not found, then this is handled; it assumes the user is already logged in
            """

            ' Open uri - if authentication is required this should automatically redirect to login '
            self.test_context.get(redirect_to_uri_on_login)

            try:
                self.test_context.implicitly_wait(4)

                elem = self.test_context.find_element_by_id("auth_user_email")
                elem.send_keys("test@localhost")
                #elem.send_keys(Keys.TAB)

                elem = self.test_context.find_element_by_id("auth_user_password")
                elem.send_keys("co2m1c")

                ' submit the form '
                elem.send_keys(Keys.RETURN)


            except Exception as e:
                ' if elements are not found then this will handle the exception assuming user is already logged in '
                print('try_login handled - already logged in (probably) - {}'.format(e.args))
                pass


        def do_log_in(self, redirect_to_uri_on_login):
            """
            Makes an attempt to log in, if the page has been redirected.
            If the inputs for login are not found, then this is handled; it assumes the user is already logged in
            """
            login_uri = "http://dev.computersciencesow.net:8000/schemeofwork/default/user/login"

            ' Open uri - if authentication is required this should automatically redirect to login '
            self.test_context.get("{}?_next={}".format(login_uri, redirect_to_uri_on_login))


            try:
                self.test_context.implicitly_wait(4)

                elem = self.test_context.find_element_by_id("auth_user_email")
                elem.send_keys("test@localhost")
                #elem.send_keys(Keys.TAB)

                elem = self.test_context.find_element_by_id("auth_user_password")
                elem.send_keys("co2m1c")

                ' submit the form '
                elem.send_keys(Keys.RETURN)

            except Exception as e:
                ' if elements are not found then this will handle the exception assuming user is already logged in '
                print('try_login handled - already logged in (probably) - {}'.format(e.args))
                pass

