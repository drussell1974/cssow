from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningobjective_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/index/{}/{}".format(self.test_scheme_of_work_id, self.test_lesson_id))
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Data Representation: Sound', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.')


    def test_page__should_have__sidebar_and_selected_lesson(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_id('nav-link-lesson-{}'.format(self.test_lesson_id))

        # assert
        self.assertEqual("", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_lessons_index(self):
        # setup

        self.test_context.find_element_by_id('lnk-bc-lessons').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_whiteboard_view(self):
        # setup

        self.test_context.find_element_by_id('lnk-whiteboard_view').click()
        self.test_context.implicitly_wait(4)

        # assert (TEST parent page is still open)
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Data Representation: Sound', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.')

