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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute', wait=2)
        self.assertPageShouldHaveGroupHeading("Academic year")
        self.assertFooterContextText("Finibus Bonorum et Malorum")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
