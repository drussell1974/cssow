from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_path = "/schemesofwork/{}/lessons/{}/learningobjectives".format(self.test_scheme_of_work_id, self.test_lesson_id)
        self.test_context.get(self.root_uri + self.test_path)

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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture; CISC and RISC')


    def test_page__should_have__sidebar_and_selected_lesson(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_id("nav-link-learning-episode-{}".format(self.test_lesson_id))
        
        # assert
        self.assertEqual("Types of CPU architecture", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__should_have__group_heading(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Learning objectives", elem.text)


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_lessons_index(self):
        # setup

        self.test_context.find_element_by_id('lnk-bc-lessons').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__breadcrumb__navigate_to_whiteboard_view(self):
        # setup

        self.test_context.find_element_by_id('lnk-whiteboard_view').click()
        self.test_context.implicitly_wait(4)

        # assert (TEST parent page is still open)
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture; CISC and RISC')


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(0, result, "number of elements not as expected")


    def test_page__show_published_and_owned(self):
        # setup
        self.do_log_in(redirect_to_uri_on_login=self.test_path)

        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(0, result, "number of elements not as expected")