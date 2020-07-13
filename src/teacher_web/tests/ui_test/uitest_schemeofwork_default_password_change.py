from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_default_change_password(UITestCase):

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

        self.test_context.find_element_by_id("btn-password_change").click()

        # assert
        # TODO: set title
        self.assertWebPageTitleAndHeadings('', 'Reset password', 'Enter a new password')

