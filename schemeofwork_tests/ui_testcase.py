from unittest import TestCase

class UITestCase(TestCase):
        def assertWebPageTitleAndHeadings(self, title, h1_site_heading, subheading):
                # assert - title
                self.assertEqual(title, self.test_context.title)
                # assert - site-heading
                self.assertEqual(h1_site_heading, self.test_context.find_element_by_tag_name("h1").text)
                # test - subheading
                self.assertEqual(subheading, self.test_context.find_element_by_class_name("subheading").text)
