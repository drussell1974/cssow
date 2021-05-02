from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_department_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department")
        self.wait()

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute')
        #self.assertPageShouldHaveGroupHeading("Departments") index page no heading
        self.assertFooterContextText("Finibus Bonorum et Malorum")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


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
        self.assertPageShouldHaveGroupHeading("")


    def test_page__post_preview__item__navigate_to_schemesofwork(self):
        # setup
        self.test_context.find_element_by_id('lnk-institute-departments--{}'.format(self.test_institute_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute', wait=4)
        #self.assertPageShouldHaveGroupHeading("") index page no heading
        

    @unittest.skip("not implemented - permissions error")
    def test_page__submenu__navigate_to_department_new(self):
        # setup
        #self.try_log_in(self.root_uri + "/schemesofwork")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'x', 'y')
        self.assertPageShouldHaveGroupHeading("")
