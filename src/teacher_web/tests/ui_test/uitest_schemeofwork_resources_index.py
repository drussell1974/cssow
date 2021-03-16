from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_resources_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources")
        

    def tearDown(self):
        
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        self.assertFooterContextText("Computer Science - Finibus Bonorum et Malorum")


    def test_page__should_have__sidebar_and_selected_lesson(self):
        # test
        elem = self.test_context.find_element_by_id("nav-link-lesson-{}".format(self.test_lesson_id))
        
        # assert
        self.assertEqual("Types of CPU architecture", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__should_have__group_heading(self):
        # test        
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Resources", elem.text)


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


    def test_page__breadcrumb__navigate_to_whiteboard_view(self):
        # setup

        self.test_context.find_element_by_id('lnk-whiteboard_view').click()
        
        # assert (TEST parent page is still open)
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(4, result, "number of elements not as expected")


    def test_page__show_published_and_owned(self):
        # setup

        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(4, result, "number of elements not as expected")


    def test_page__should_have_sidenav__showing_options_for_this_lesson(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This lesson", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_other_lessons(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=3, expected_title="Other lessons", expected_no_of_items=25)