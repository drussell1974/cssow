from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_institute_academic_year_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/academic-years")
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute')
        self.assertFooterContextText("Finibus Bonorum et Malorum")
        self.assertPageShouldHaveGroupHeading("Academic years")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(False)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
        self.assertNavTabsShouldBeInstitute()
        

    def test_page__post_preview__item__navigate_to_academic_year__edit(self):
        # setup
        self.test_context.find_element_by_id('lnk-institute-academic_year--{}'.format(2020)).click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute', wait=4)
        self.assertPageShouldHaveGroupHeading("Academic year")
        

    def test_page__submenu__navigate_to_academic_year_new(self):
        # setup
        #self.try_log_in(self.root_uri + "/schemesofwork")

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Finibus Bonorum et Malorum', 'Institute')
        self.assertPageShouldHaveGroupHeading("Academic year")