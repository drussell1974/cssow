from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_ks123pathway_edit_create_new_page_navigation(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/pathways/new")
        # TODO: improve performance
        self.wait(s=2)


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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Computer Science', 'Create new pathway objective', wait=2)
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")


    """ Breadcrumb """

    def test_page__breadcrumb__navigate_to_ks123pathway_index(self):
        #test
        elem = self.test_context.find_element_by_id('btn-bc-ks123pathway')
        self.assertEqual("Pathways", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Computer Science', 'KS123 Pathways')
