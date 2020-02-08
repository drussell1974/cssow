from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.try_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/lesson-plan".format(self.test_scheme_of_work_id, self.test_lesson_id))
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




