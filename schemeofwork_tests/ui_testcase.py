from unittest import TestCase
from selenium.webdriver.common.keys import Keys

class UITestCase(TestCase):

        root_uri = "http://127.0.0.1:8000/schemeofwork/"

        web_pages_titles_and_headings = {
                'default/index':['schemeofwork', 'Computing Schemes of work and lessons', 'Computing schemes of work lessons across all key stages'],
                'schemesofwork/index':['schemeofwork', 'Schemes of work', 'Our shared schemes of work by key stage'],
                'schemesofwork/edit/new':['schemeofwork', 'Scheme of work', 'Create a new scheme of work'],
                'schemesofwork/edit':['schemeofwork', 'Selenium UI Test', 'KS1 - AQA'],
                'learningepisode/index/new':['schemeofwork', "Learning episodes", 'for should_redirect_to_index_if_valid'],
                'learningepisode/index/76':['schemeofwork', "Learning episodes", 'for Selenium UI Test'],
                'learningepisode/edit/new':['schemeofwork', "Learning episode", 'for Selenium UI Test'],
                'learningepisode/edit/76':['schemeofwork', 'MUST SHOW TITLE FOR id=11', 'MUST SHOW SUBHEADING HERE FOR id=11'],
                'learningobjective/index':['schemeofwork', 'Learning objectives', 'for Selenium UI Test - Week 1 - Problem solving'],
                'learningobjective/edit/new':['schemeofwork', 'MUST SHOW TITLE FOR id=11', 'MUST SHOW SUBHEADING FOR id=11'],
                'learningobjective/edit':['schemeofwork', 'MUST SHOW TITLE FOR id=11', 'MUST SHOW SUBHEADING HERE FOR id=11'],
                'default/user/login':['schemeofwork', 'Log In', 'Register to create schemes of work and lessons'],
        }


        def assertWebPageTitleAndHeadingsByRoute(self, route):
                values = self.web_pages_titles_and_headings[route]

                # assert - title
                self.assertEqual(values[0], self.test_context.title, '"{}{}" page title should be "{}"'.format(self.root_uri, route, values[0]))
                # assert - site-heading
                self.assertEqual(values[1], self.test_context.find_element_by_tag_name("h1").text, '"{}{}" heading (h1) should be "{}"'.format(self.root_uri, route, values[1]))
                # test - subheading
                self.assertEqual(values[2], self.test_context.find_element_by_class_name("subheading").text, '"{}{}" subheading should be "{}""'.format(self.root_uri, route, values[2]))


        def try_log_in(self, redirect_to_uri_on_login):
                """
                Makes an attempt to log in, if the page has been redirected.
                If the inputs for login are not found, then this is handled; it assumes the user is already logged in
                """

                ' Open uri - if authentication is required this should automatically redirect to login '
                self.test_context.get(redirect_to_uri_on_login)

                try:
                        ' sleep to give time for browser to respond before attempting login '
                        import time
                        time.sleep(3)

                        elem = self.test_context.find_element_by_id("auth_user_email")
                        elem.send_keys("dave@jazzthecat.co.uk")
                        #elem.send_keys(Keys.TAB)

                        elem = self.test_context.find_element_by_id("auth_user_password")
                        elem.send_keys("co2m1c")

                        ' submit the form '
                        elem.send_keys(Keys.RETURN)

                        ' sleep to give time for browser to respond '
                        # SHOULD REDIRECT
                        import time
                        time.sleep(3)

                except Exception as e:
                        ' if elements are not found then this will handle the exception assuming user is already logged in '
                        print('try_login handled - already logged in (probably) - {}'.format(e.args))
                        pass


        def do_log_in(self, redirect_to_uri_on_login):
                """
                Makes an attempt to log in, if the page has been redirected.
                If the inputs for login are not found, then this is handled; it assumes the user is already logged in
                """
                login_uri = "http://127.0.0.1:8000/schemeofwork/default/user/login"

                ' Open uri - if authentication is required this should automatically redirect to login '
                self.test_context.get("{}?_next={}".format(login_uri, redirect_to_uri_on_login))


                try:
                        ' sleep to give time for browser to respond before attempting login '
                        import time
                        time.sleep(3)

                        elem = self.test_context.find_element_by_id("auth_user_email")
                        elem.send_keys("dave@jazzthecat.co.uk")
                        #elem.send_keys(Keys.TAB)

                        elem = self.test_context.find_element_by_id("auth_user_password")
                        elem.send_keys("co2m1c")

                        ' submit the form '
                        elem.send_keys(Keys.RETURN)

                        ' sleep to give time for browser to respond '
                        # SHOULD REDIRECT
                        import time
                        time.sleep(3)

                except Exception as e:
                        ' if elements are not found then this will handle the exception assuming user is already logged in '
                        print('try_login handled - already logged in (probably) - {}'.format(e.args))
                        pass

