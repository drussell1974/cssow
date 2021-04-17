from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lessonschedule_edit_create_new_page_navigation(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/schedules/new")
        # TODO: improve performance
        self.wait(s=4)


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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Create schedule for Types of CPU architecture')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")


    """ Breadcrumb """


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('btn-bc-schemes_of_work')
        self.assertEqual("Schemes of Work", elem.text)

        # test
        elem.click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_schemesofwork_schedule(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemeofwork_schedule')
        self.assertEqual("Schedule", elem.text)

        # test
        elem.click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheduled lessons')


    def test_page__breadcrumb__navigate_to_lesson_index(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-lessons')
        self.assertEqual("Lessons", elem.text)

        # test
        elem.click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__breadcrumb__navigate_to_lesson_schedule(self):
        #test
        elem = self.test_context.find_element_by_id('lnk-bc-lesson_schedule')
        self.assertEqual("Schedule", elem.text)

        # test
        elem.click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Scheduled lessons')
