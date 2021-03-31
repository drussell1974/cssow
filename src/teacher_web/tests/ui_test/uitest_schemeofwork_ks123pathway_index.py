from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_ks123pathway_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/pathways")
        self.wait(s=1)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Computer Science', 'KS123 Pathways')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")


    def test_page__should_have__group_heading(self):
        # test
        elem = self.test_context.find_element_by_class_name('group-heading')

        # assert
        self.assertEqual("Pathways", elem.text)


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__show_published_only(self):
        # setup
        section = self.test_context.find_elements_by_class_name('card-ks123pathway')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(152, result, "number of elements not as expected")

