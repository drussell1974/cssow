from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningobjective_edit_create_existing_navigation(UITestCase):

    test_context = WebBrowserContext()


    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/edit?id={}&lesson_id={}&scheme_of_work_id={}".format(self.test_learning_objective_id,  self.test_lesson_id, self.test_scheme_of_work_id))


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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Learning objective', 'A-Level Computer Science - Lesson 1 - Programming and development')


    """ Breadcrumb """


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("Schemes of Work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_lesson_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-lessons')
        self.assertEqual("Lessons", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_learningobjective_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_objectives')
        self.assertEqual("Objectives", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Data Representation: Sound', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.')
