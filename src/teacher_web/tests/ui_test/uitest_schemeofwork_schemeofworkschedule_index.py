from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_schemeofworkschedule_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/schedules")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheduled lessons')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Schedule 2020/2021")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(True)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_other_lessons(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="Department", expected_no_of_items=3)


    # card-scheduled_lesson

    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('badge-primary')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(1, result, "number of elements not as expected")


    def test_page__show_previous_academic_year(self):
        # setup
        ' selected_year - select previous academic year '
        elem = self.test_context.find_element_by_css_selector("#ctl-academic_year > option:nth-child(1)")
        elem.click()

        self.wait(s=4)

        # assert

        section = self.test_context.find_elements_by_class_name('badge-primary')

        result = len(section)

        # assert
        self.assertEqual(1, result, "number of elements not as expected")
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheduled lessons')
        self.assertEqual("Schedule 2019/2020", self.test_context.find_element_by_class_name('group-heading').text)


    def test_page__show_current_academic_year_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('badge-primary')

        # test
        result = len(section)

        # assert
        self.assertEqual(1, result, "number of elements not as expected")

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheduled lessons')
        self.assertEqual("Schedule 2020/2021", self.test_context.find_element_by_class_name('group-heading').text)


    def test_page__show_new(self):
        # setup
        elem = self.test_context.find_element_by_css_selector('.fc-add_scheduled_lesson-button')

        elem.click()
        self.wait(s=2)

        # assert

        elem = self.test_context.find_element_by_css_selector('.modal-title#scheduledLessonModalLabel')
        self.assertEqual("New Scheduled lesson", elem.text)

