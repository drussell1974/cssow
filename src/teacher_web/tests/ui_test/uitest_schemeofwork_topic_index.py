from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_topic_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/topics")
        self.wait(s=1)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Computer Science', 'Department')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Topics")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
        self.assertNavTabsShouldBeDepartment()


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-topic')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(72, result, "number of elements not as expected")

