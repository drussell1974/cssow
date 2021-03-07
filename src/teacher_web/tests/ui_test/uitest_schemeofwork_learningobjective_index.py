from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_learningobjective_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives", wait=2)


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
        self.assertFooterContextText("test@localhost Computer Science")


    def test_page__should_have__sidebar_and_selected_lesson(self):
        # test
        #self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_id("nav-link-lesson-{}".format(self.test_lesson_id))
        
        # assert
        self.assertEqual("Types of CPU architecture", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__should_have__group_heading(self):
        # test
        #self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Learning objectives", elem.text)


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()
        
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_lessons_index(self):
        # setup

        self.test_context.find_element_by_id('lnk-bc-lessons').click()
        self.wait(s=1)

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
        self.assertEqual(8, result, "number of elements not as expected")


    def test_page__show_published_and_owned(self):
        # setup
        
        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(8, result, "number of elements not as expected")


    def test_page__should_display_descriptions_and_notes(self):
        # setup
        # test
        
        elem = self.test_context.find_element_by_id(f"btn-collapseNotes--{self.test_learning_objective_id}")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click() # reveal notes

        elem_description = self.test_context.find_element_by_class_name(f'post-preview--{self.test_learning_objective_id} h3.post-title')
        elem_notes = self.test_context.find_element_by_class_name(f'post-preview--{self.test_learning_objective_id} p.preserve-linebreak')
        
        # assert
        self.assertEqual("Explain what happens to inactive processes and what is the purpose of managing these inactive processes", elem_description.text)
        # show only first 500 with ellipse
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet feugiat lectus. Duis posuere tristique vulputate. Suspendisse at tristique magna, id interdum neque. Proin et nisl et justo tincidunt ullamcorper nec vitae urna. Etiam molestie porta dolor. Nulla iaculis consequat volutpat. Ut ac erat tempus, facilisis felis eleifend, porttitor ipsum. Proin porttitor ex et imperdiet venenatis. Suspendisse eleifend ut libero nec tincidunt. Donec molestie metus nunc, quis congue dolor aliquet nec. Integer lacus arcu, dignissim eget vulputate vel, semper vulputate arcu. Nam fringilla morbi.", elem_notes.text)


    def test_page__should_have_sidenav__showing_options_for_this_lesson(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This lesson", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_other_lessons(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=3, expected_title="Other lessons", expected_no_of_items=25)
