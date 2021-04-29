from ui_testcase import UITestCase, WebBrowserContext

class uitest_institute_academic_year_edit_create_new_page_navigation(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/academic-years/new")
        # TODO: improve performance
        self.wait(s=2)


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    """ Test content """

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        # NOTE: This increments to next available academic year
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'New academic year 2022/2023', wait=2)
        self.assertFooterContextText("Finibus Bonorum et Malorum")


    """ Breadcrumb """

    def test_page__breadcrumb__navigate_to_institute_index(self):
        #test
        elem = self.test_context.find_element_by_id('btn-bc-institute')
        self.assertEqual("Institute", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Institutes')
        

    def test_page__breadcrumb__navigate_to_academic_year_index(self):
        #test
        elem = self.test_context.find_element_by_id('btn-bc-academic_year')
        self.assertEqual("Academic years", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Academic years', wait=2)
