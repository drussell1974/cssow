from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_institute_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute")
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Institutes')
        

    @unittest.skip("overlay isssue causing - low priority test - selenium.common.exceptions.ElementNotInteractableException: could not be scrolled into view")
    def test_page__navigate_to_lesson_index(self):

        # setup

        elem = self.test_context.find_element_by_id("lnk-schemeofwork-127")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'GCSE Computer Science 9-1', "Lessons")


    def test_page__breadcrumb(self):
        #test
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


    def test_page__topnav__navigate_to_home(self):
        # setup
        self.test_context.find_element_by_id('btn-topnav-home').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')


    def test_page__post_preview__item__navigate_to_departments(self):
        # setup
        self.test_context.find_element_by_id('lnk-institute-departments--{}'.format(self.test_institute_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Departments')
