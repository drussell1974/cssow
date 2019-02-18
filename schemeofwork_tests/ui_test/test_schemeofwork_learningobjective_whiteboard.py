from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepsiode_whiteboard(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/whiteboard_view/{}/{}".format(self.test_scheme_of_work_id, self.test_learning_episode_id))
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Learn Computer Science', 'Data Representation: Sound', 'Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit. Nam Convallis Volutpat.')


    def test_page__should_have__key_words(self):
        # test
        elem = self.test_context.find_element_by_id('heading-key_words')

        # assert
        self.assertEqual("Today's Keywords", elem.text)


    def test_page__should_have__prior_learning_objectives(self):
        # test
        elem = self.test_context.find_element_by_id('heading-prior_learning_objectives')

        # assert
        self.assertEqual("Prior Learning", elem.text)


    def test_page__should_have__learning_objectives(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_objectives')

        # assert
        self.assertEqual("Today's Learning Objectives", elem.text)


    def test_page__should_have__learning_materials(self):
        # test
        elem = self.test_context.find_element_by_id('heading-learning_materials')

        # assert
        self.assertEqual("Learning Materials", elem.text)




