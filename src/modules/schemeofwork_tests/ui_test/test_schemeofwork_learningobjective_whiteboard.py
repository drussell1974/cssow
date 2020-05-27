from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_lessonobjective_whiteboard(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/whiteboard_view/{}/{}".format(self.test_scheme_of_work_id, self.test_lesson_id))
        self.test_context.implicitly_wait(4)
        self.wait(20)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Data Representation: Sound', 'Data Representation: Sound', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.')


    def test_page__should_have__key_words(self):
        # test
        elem = self.test_context.find_element_by_id('heading-key_words')

        # assert
        self.assertEqual("Keywords", elem.text)


    def test_page__should_have__prior_learning_objectives(self):
        # test
        elem = self.test_context.find_element_by_id('heading-prior_learning_objectives')

        # assert
        self.assertEqual("Prior learning", elem.text)


    def test_page__should_have__learning_objectives(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_objectives')

        # assert
        self.assertEqual("Learning objectives", elem.text)


    def test_page__should_have__learning_materials(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_materials')

        # assert
        self.assertEqual("Learning materials", elem.text)




