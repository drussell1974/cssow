from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_content_edit_existing_page_navigation(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content/{self.test_content_id}/edit")

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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheme of work')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Curriculum")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(True)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
