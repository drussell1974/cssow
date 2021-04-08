from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_institute_schedule(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/schedule")
        self.wait()


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Schedule')
        

    @skip("# TODO: #329 create drop down to view institutes departments schemesofwork - changes context")
    def test_page__breadcrumb__navigate_to_departments_all(self):
        # setup
        self.test_context.find_element_by_id('btn-topnav-departments_all').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_home(self):
        # setup
        self.test_context.find_element_by_id('btn-topnav-home').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')

