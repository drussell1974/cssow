from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_schemesofwork_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/schemesofwork/index")
        self.test_context.implicitly_wait(4)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__navigate_to_lesson_index(self):

        # setup

        elem = self.test_context.find_element_by_id("lnk-schemeofwork-58")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'KS3 Computing (Track 1)')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def not_test_page__submenu__navigate_to_schemesofwork_new(self):
        # setup
        self.try_log_in(self.root_uri + "/schemeofwork/schemesofwork/index")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', '', '')





