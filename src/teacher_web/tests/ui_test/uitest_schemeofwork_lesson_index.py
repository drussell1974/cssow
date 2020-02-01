from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lesson_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_path = "/schemesofwork/{}/lessons".format(self.test_scheme_of_work_id)

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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # arrange
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()


        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__submenu__navigate_to_lesson_new(self):
        # setup
        self.do_log_in(self.test_path)

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'New')


    def test_page__should_have_sidenav(self):
        # arrange
        elem = self.test_context.find_element_by_id('sidebarNav')

        # act

        # assert
        self.assertIsNotNone(elem)


    def test_page__should_have_sidenav_with_three_items(self):
        # arrange
        elems = self.test_context.find_elements_by_class_name('nav-item')
        
        # act

        # assert
        self.assertEqual(6, len(elems))


    def test_page__show_published_only(self):
        # arrange
        section = self.test_context.find_elements_by_class_name('post-preview')
        # assert
        result = len(section)
        self.assertEqual(27, result, "number of elements not as expected")


    def test_page__show_published_and_owned(self):
        # setup
        self.do_log_in(redirect_to_uri_on_login=self.test_path)

        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert    
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(27, result, "number of elements not as expected")
        

