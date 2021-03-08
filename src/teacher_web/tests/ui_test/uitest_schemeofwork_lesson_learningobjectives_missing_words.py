from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lesson_learningobjectives_missing_words(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/missing-words")
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Algorithms')


    def test_page__should_have__learning_objectives(self):
        # test
        elems = self.test_context.find_elements_by_class_name("learning-objective--card")

        # assert
        self.assertEqual(2, len(elems))


    def test_page__should_preview_missing_words_challenge(self):
        # setup
        # test

        # preview missing notes

        elem = self.test_context.find_element_by_css_selector(f"#learning_objective{self.test_learning_objective_id} .btn-challenge")
        ' Ensure element is visible '
        elem.click() # preview missing words
        self.wait(s=1)
        
        elem_notes = self.test_context.find_element_by_css_selector(f'#learning_objective{self.test_learning_objective_id} p.notes')
        
        # assert
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet feugiat lectus. Duis posuere tristique vulputate. Suspendisse at tristique magna, id interdum neque. ____ et nisl et justo tincidunt ullamcorper nec vitae urna. Etiam molestie porta dolor. Nulla iaculis consequat volutpat. Ut ac erat tempus, facilisis felis ____ eleifend, ______________ porttitor ex et imperdiet venenatis. Suspendisse eleifend ut libero nec tincidunt. Donec molestie metus ___, quis congue dolor aliquet nec. Integer lacus arcu, dignissim eget ____________, semper vulputate arcu. Nam fringilla morbi.", elem_notes.text)
