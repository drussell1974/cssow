from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_default_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork")
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test
        self
        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Computing Schemes Of Work And Lessons', 'Computing schemes of work lessons across all key stages')


    def test_page__navigate_to_all_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('btn-all-schemes-of-work').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes Of Work', 'Our shared schemes of work by key stage')


    def test_page__show_only_published_latest_schemesofwork(self):
        # setup
        section = self.test_context.find_elements_by_class_name('post-preview-schemeofwork')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(4, result, "number of elements not as expected")


    def test_page__show_published_and_owned_latest_schemesofwork(self):
        # setup
        self.do_log_in(redirect_to_uri_on_login="http://dev.computersciencesow.net:8000/schemeofwork")

        section = self.test_context.find_elements_by_class_name('post-preview-schemeofwork')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(5, result, "number of elements not as expected")








