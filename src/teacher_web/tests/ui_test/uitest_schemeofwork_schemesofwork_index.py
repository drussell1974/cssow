from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofwork_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork")

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Lessons")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
        self.assertNavTabsShouldBeDepartment()


    def test_page__post_preview__item__navigate_to_lessons(self):
        # setup
        self.test_context.find_element_by_id('lnk-schemeofwork-lessons--{}'.format(self.test_scheme_of_work_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
        

    def test_page__post_preview__item__navigate_to_curriculum(self):
        # setup
        self.test_context.find_element_by_id('lnk-schemeofwork-curriculum--{}'.format(self.test_scheme_of_work_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Curriculum')
        

    def test_page__post_preview__item__navigate_to_keywords(self):
        # setup
        self.test_context.find_element_by_id('lnk-schemeofwork-keywords--{}'.format(self.test_scheme_of_work_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')
        

    def test_page__post_preview__item__navigate_to_schedule(self):
        # setup
        self.test_context.find_element_by_id('lnk-schemeofwork-schedule--{}'.format(self.test_scheme_of_work_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Scheduled lessons')
        

    def not_test_page__submenu__navigate_to_schemesofwork_new(self):
        # setup
        self.try_log_in(self.root_uri + "/schemesofwork")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', '', '')





