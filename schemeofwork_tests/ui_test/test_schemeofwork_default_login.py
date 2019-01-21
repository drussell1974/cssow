from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_default_login(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/default/user/login")
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # setup

        self.test_context.find_element_by_id("btn-login").click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Log In', 'register to create schemes of work and lessons')

