from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepisode_edit_existing_page_navigation(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningepisode/edit?id={}&scheme_of_work_id={}".format(self.test_learning_episode_id, self.test_scheme_of_work_id))

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test content """

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Episode', 'for a-level computer science programming and development - week 1')


    """ Breadcrumb """

    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("schemes of work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork','Schemes Of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_learningepisode_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_episodes')
        self.assertEqual("episodes", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Episodes', 'for A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_learningobjective_index(self):

        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_objectives')
        self.assertEqual("objectives", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning Objectives', 'for A-Level Computer Science - Week 1 - Programming and development')


    def test_page__should_have_related_topic_ids(self):

        # test
        elems = self.test_context.find_elements_by_class_name('form-check-label')

        # assert
        self.assertTrue(16, len(elems))


    def test_page__should_have_checked_related_topic_id(self):

        # test
        elem = self.test_context.find_element_by_id('ctl-related_topic_id42')

        # assert
        self.assertTrue(elem.is_selected())

    def test_page__should_have_unchecked_related_topic_id(self):

        # test
        elem = self.test_context.find_element_by_id('ctl-related_topic_id57')

        # assert
        self.assertFalse(elem.is_selected())


    def test_page__should_have_disabled_related_topic_id(self):

        # test
        elem = self.test_context.find_element_by_id('ctl-related_topic_id42')

        # assert
        self.assertFalse(elem.is_enabled())


    def test_page__should_have_disabled_related_topic_id(self):

        # test
        elem = self.test_context.find_element_by_id('ctl-related_topic_id57')

        # asserts
        self.assertTrue(elem.is_enabled())
