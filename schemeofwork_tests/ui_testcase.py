from unittest import TestCase
from selenium import webdriver

class UITestCase(TestCase):

        root_uri = "http://127.0.0.1:8000/schemeofwork/"

        web_pages_titles_and_headings = {
                'default/index':['schemeofwork', 'Computing Schemes of work and lessons', 'Computing schemes of work lessons across all key stages'],
                'schemesofwork/index':['schemeofwork', 'Schemes of work', 'Our shared schemes of work by key stage'],
                'learningepisode/index':['schemeofwork', "Learning episodes", 'for A-Level Computer Science'],
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

        def _log_in(self):
                # setup

                self.test_context.find_element_by_id("btn-login").click()
                ' sleep to give time for browser to respond '
                import time
                time.sleep(3)

                elem = self.test_context.find_element_by_id("auth_user_email")
                elem.send_keys("dave@jazzthecat.co.uk")
                elem.send_keys(Keys.TAB)
                elem = self.test_context.find_element_by_id("auth_user_password")
                elem.send_keys("co2m1c")
                elem.send_keys(Keys.RETURN)

                ' sleep to give time for browser to respond '
                import time
                time.sleep(3)
