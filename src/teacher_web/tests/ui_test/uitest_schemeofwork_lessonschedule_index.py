from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lessonschedule_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/schedules")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Scheduled lessons')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")


    def test_page__should_have__sidebar_and_selected_lesson(self):
        # test
        elem = self.find_element_by_id__with_explicit_wait("nav-link-lesson-{}".format(self.test_lesson_id), wait=4)
        
        # assert
        self.assertEqual("Types of CPU architecture", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__should_have__group_heading(self):
        # test
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Schedule 2020/2021", elem.text)


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_lessons_index(self):
        # setup

        self.test_context.find_element_by_id('lnk-bc-lessons').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-keyword')

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

        section = self.test_context.find_elements_by_class_name('card-keyword')

        result = len(section)

        # assert
        self.assertEqual(0, result, "number of elements not as expected")
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Scheduled lessons')
        self.assertEqual("Schedule 2019/2020", self.test_context.find_element_by_class_name('group-heading').text)


    def test_page__show_current_academic_year_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-keyword')

        # test
        result = len(section)

        # assert
        self.assertEqual(1, result, "number of elements not as expected")

        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Scheduled lessons')
        self.assertEqual("Schedule 2020/2021", self.test_context.find_element_by_class_name('group-heading').text)


    def test_page__show_edit(self):
        # setup
        elem = self.test_context.find_element_by_id(f'lnk-edit-lesson_schedule--{self.test_lesson_schedule_id}')

        elem.click()
        
        # assert
        self.assertWebPageTitleAndHeadings(title="Dave Russell - Teach Computer Science", h1="Types of CPU architecture", subheading="Edit scheduled lesson Types of CPU architecture for 8u", wait=2)
        

    def test_page__show_new(self):
        # setup
        elem = self.test_context.find_element_by_id(f'btn-new')

        elem.click()
        
        # assert
        self.assertWebPageTitleAndHeadings(title="Dave Russell - Teach Computer Science", h1="Types of CPU architecture", subheading="Create schedule for Types of CPU architecture", wait=2)
        

    def test_page__should_have_sidenav__showing_options_for_this_lesson(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This lesson", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_other_lessons(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=3, expected_title="Other lessons", expected_no_of_items=25)
