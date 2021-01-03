from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_default_password_change(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri)
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # setup

        elem = self.test_context.find_element_by_id("btn-profile")
        elem.click()

        elem = self.test_context.find_element_by_id("btn-password_change")
        elem.click()

        self.wait(s=2)

        # assert
        self.assertWebPageTitleAndHeadings('', 'Account', 'Change password')
        
