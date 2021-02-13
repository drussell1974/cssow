from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_schemeofwork_lesson_whiteboard(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{}/lessons/{}/whiteboard".format(self.test_scheme_of_work_id, self.test_lesson_id))

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
