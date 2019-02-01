from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/index/{}/{}".format(self.test_scheme_of_work_id, self.test_learning_episode_id))
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Objectives', 'for A-Level Computer Science - Lesson 1 - Programming and development')


    def test_page__should_have__sidebar_and_selected_learning_episode(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_id('nav-link-learning-episode-{}'.format(self.test_learning_episode_id))

        # assert
        self.assertEqual("", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))



    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Schemes Of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_learningepisodes_index(self):
        # setup

        self.test_context.find_element_by_id('lnk-bc-learning_episodes').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Lessons', 'for A-Level Computer Science')


    def not_test_page__submenu__navigate_to_learningepisode_new(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/index/{}/{}".format(self.test_scheme_of_work_id, self.test_learning_episode_id))

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', '', '')




