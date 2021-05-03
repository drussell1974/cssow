from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lesson_whiteboard(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/schedules/{self.test_lesson_schedule_id}/whiteboard")
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


    def test_page__should_have__key_words(self):
        # test
        elem = self.test_context.find_element_by_id('heading-key_words')
        elems = self.test_context.find_elements_by_class_name("keyword")

        # assert
        self.assertEqual("Keywords", elem.text)
        self.assertEqual(3, len(elems))


    def test_page__should_have__learning_objectives(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_objectives')
        elems = self.test_context.find_elements_by_class_name("learning_objective-item")

        # assert
        self.assertEqual("Learning objectives", elem.text)
        self.assertEqual(8, len(elems))


    def test_page__should_have__learning_materials(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_materials')
        elems = self.test_context.find_elements_by_class_name("learning-material-item")

        # assert
        self.assertEqual("Learning materials", elem.text)
        self.assertEqual(4, len(elems))


    def test_page__should_preview_missing_words_challenge(self):
        # setup
        # test
        
        elem = self.test_context.find_element_by_id(f"expand-learning_objective--{self.test_learning_objective_id}")
        elem.click() # reveal notes
        self.wait(s=1)

        # preview missing notes

        elem = self.test_context.find_element_by_css_selector(f"#collapse-learning_objective--{self.test_learning_objective_id} .btn-challenge")
        elem.click() # preview missing words
        self.wait(s=1)
        
        elem_notes = self.test_context.find_element_by_css_selector(f'#collapse-learning_objective--{self.test_learning_objective_id} p.notes')
        elem_missing_words_challenge = self.test_context.find_element_by_id(f'missing-words-challenge--{self.test_learning_objective_id}')

        # assert
        self.maxDiff = None
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet feugiat lectus. Duis posuere tristique vulputate. Suspendisse at tristique magna, id interdum neque. ____ et nisl et justo tincidunt ullamcorper nec vitae urna. Etiam molestie porta dolor. Nulla iaculis consequat volutpat. Ut ac erat tempus, facilisis felis ____ eleifend, ______________ porttitor ex et imperdiet venenatis. Suspendisse eleifend ut libero nec tincidunt. Donec molestie metus ___, quis congue dolor aliquet nec. Integer lacus arcu, dignissim eget ____________, semper vulputate arcu. Nam fringilla morbi.", elem_notes.text)
        self.assertEqual("nunc,porttitor ipsum,PROIN,vulputate vel", elem_missing_words_challenge.text)
