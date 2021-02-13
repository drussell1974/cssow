from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningobjective_index_with_login(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__submenu__navigate_to_lesson_new(self):
        # setup

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Create new learning objective for Types of CPU architecture')

