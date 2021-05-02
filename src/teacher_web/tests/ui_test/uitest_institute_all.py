from ui_testcase import UITestCase, WebBrowserContext
from unittest import skip

class uitest_institute_all(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/all")
        self.wait()


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')
        #self.assertPageShouldHaveGroupHeading("") index page no heading
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)


    @skip("overlay isssue causing - low priority test - selenium.common.exceptions.ElementNotInteractableException: could not be scrolled into view")
    def test_page__navigate_to_lesson_index(self):

        # setup

        elem = self.test_context.find_element_by_id("lnk-schemeofwork-127")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'GCSE Computer Science 9-1', "Lessons")


    def test_page__post_preview__item__navigate_to_departments(self):
        # setup
        self.test_context.find_element_by_id('lnk-institute-departments--{}'.format(self.test_institute_id)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute')
        self.assertPageShouldHaveGroupHeading("Departments")
    

    def not_test_page__submenu__navigate_to_schemesofwork_new(self):
        # setup
        self.try_log_in(self.root_uri + "/schemesofwork")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', '', '')





