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
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Learning objectives")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(True)
        self.assertBreadcrumbShouldHaveLessonsIndex(True)
        self.assertNavTabsShouldBeLesson()


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


    def test_page__should_display_description(self):
        # setup
        # test
        
        #elem = self.test_context.find_element_by_id(f"btn-collapseNotes--{self.test_learning_objective_id}")

        elem_description = self.test_context.find_element_by_class_name(f'post-preview--{self.test_learning_objective_id} h3.post-title')
        
        # assert
        self.assertEqual("Explain what happens to inactive processes and what is the purpose of managing these inactive processes", elem_description.text)


    def test_page__should_hidden__notes__and__missing_words(self):
        # setup
        # test
        
        elem = self.test_context.find_element_by_id(f"btn-collapseNotes--{self.test_learning_objective_id}")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click() # reveal notes
        self.wait(s=1)

        elem_notes = self.test_context.find_element_by_class_name(f'post-preview--{self.test_learning_objective_id} p.notes')
        
        # assert
        
        self.maxDiff = None
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet feugiat lectus. Duis posuere tristique vulputate. Suspendisse at tristique magna, id interdum neque. Proin et nisl et justo tincidunt ullamcorper nec vitae urna. Etiam molestie porta dolor. Nulla iaculis consequat volutpat. Ut ac erat tempus, facilisis felis proin eleifend, Porttitor ipsum porttitor ex et imperdiet venenatis. Suspendisse eleifend ut libero nec tincidunt. Donec molestie metus nunc, quis congue dolor aliquet nec. Integer lacus arcu, dignissim eget vulputate vel, semper vulputate arcu. Nam fringilla morbi.", elem_notes.text)


    def test_page__should_preview_missing_words_challenge(self):
        # setup
        # test
        
        elem = self.test_context.find_element_by_id(f"btn-collapseNotes--{self.test_learning_objective_id}")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click() # reveal notes
        self.wait(s=1)

        # preview missing notes

        elem = self.test_context.find_element_by_css_selector(f"#card--class-notes--{self.test_learning_objective_id} .btn-challenge")
        ' Ensure element is visible '
        elem.click() # preview missing words
        self.wait(s=1)
        
        elem_notes = self.test_context.find_element_by_css_selector(f'#collapseNotes--{self.test_learning_objective_id} p.notes')
        elem_missing_words_challenge = self.test_context.find_element_by_css_selector(f'#collapseNotes--{self.test_learning_objective_id} p.missing-words-challenge')
        
        # assert
        self.maxDiff = None
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet feugiat lectus. Duis posuere tristique vulputate. Suspendisse at tristique magna, id interdum neque. ____ et nisl et justo tincidunt ullamcorper nec vitae urna. Etiam molestie porta dolor. Nulla iaculis consequat volutpat. Ut ac erat tempus, facilisis felis ____ eleifend, ______________ porttitor ex et imperdiet venenatis. Suspendisse eleifend ut libero nec tincidunt. Donec molestie metus ___, quis congue dolor aliquet nec. Integer lacus arcu, dignissim eget ____________, semper vulputate arcu. Nam fringilla morbi.", elem_notes.text)
        self.assertEqual("nunc,porttitor ipsum,PROIN,vulputate vel", elem_missing_words_challenge.text)
