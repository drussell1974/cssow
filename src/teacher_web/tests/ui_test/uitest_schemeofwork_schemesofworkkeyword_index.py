from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_schemesofworkkeyword_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_path = "/schemesofwork/{}/keywords".format(self.test_scheme_of_work_id)
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')


    def test_page__should_have__sidebar_and_selected_scheme_of_work(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_id("nav-link-schemeofwork-{}".format(self.test_scheme_of_work_id))
        
        # assert
        self.assertEqual("A-Level Computer Science\nKS5", elem.text)
        self.assertEqual("nav-link", elem.get_attribute("class"))


    def test_page__should_have__group_heading(self):
        # test
        self.test_context.implicitly_wait(20)
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Keywords", elem.text)


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-keyword')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(162, result, "number of elements not as expected")


    def test_page__show_published_and_owned(self):
        # setup
        self.do_log_in(redirect_to_uri_on_login=self.test_path)
        
        section = self.test_context.find_elements_by_class_name('card-keyword')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(162, result, "number of elements not as expected")


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-keyword--lessons')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(50, result, "number of elements not as expected")


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_other_lessons(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="Other schemes of work", expected_no_of_items=3)
