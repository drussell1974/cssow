from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lesson_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons")


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
        self.assertFooterContextText("Computer Science Finibus Bonorum et Malorum")
        self.assertTopNavShouldHaveHomeIndex(True)
        self.assertTopNavShouldHaveDepartmentsIndex(False)
        self.assertBreadcrumbShouldHaveDepartmentsIndex(True)
        self.assertBreadcrumbShouldHaveSchemesOfWorkIndex(True)
        self.assertBreadcrumbShouldHaveLessonsIndex(False)
        self.assertNavTabsShouldBeSchemeOfWork()


    def test_page__submenu__navigate_to_lesson_new(self):
        # setup

        # test
        self.test_context.find_element_by_id('btn-new').click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new lesson for A-Level Computer Science')


    def test_page__show_published_only(self):
        # arrange

        # array of expected items per pages

        expected_item_per_page = [10,10,5,0]

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()

        
    def test_page__post_preview__item__navigate_to_ks123pathways(self):
        # setup
        
        # click dropdown
        elem = self.test_context.find_element_by_id('lessonDropdownMenuLink--{}'.format(self.test_lesson_id))
        elem.click()
        
        # click option

        elem = self.test_context.find_element_by_id('btn-lesson-ks123pathways--{}'.format(self.test_lesson_id))

        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)

        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Select pathway for Types of CPU architecture')
    
    
    def test_page__post_preview__item__navigate_to_learning_objectives(self):
        # setup
        
        # click dropdown
        elem = self.test_context.find_element_by_id('lessonDropdownMenuLink--{}'.format(self.test_lesson_id))
        elem.click()
        
        # click option

        elem = self.test_context.find_element_by_id('btn-lesson-learningobjectives--{}'.format(self.test_lesson_id))

        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)

        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        
        
    def test_page__post_preview__item__navigate_to_resources(self):
        # setup

        # click dropdown
        elem = self.test_context.find_element_by_id('lessonDropdownMenuLink--{}'.format(self.test_lesson_id))
        elem.click()
        
        # click option

        elem = self.test_context.find_element_by_id('btn-lesson-resources--{}'.format(self.test_lesson_id))

        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)

        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        

    def test_page__post_preview__item__navigate_to_keywords(self):
        # setup
        
        # click dropdown
        elem = self.test_context.find_element_by_id('lessonDropdownMenuLink--{}'.format(self.test_lesson_id))
        elem.click()
        
        # click option

        elem = self.test_context.find_element_by_id('btn-lesson-keywords--{}'.format(self.test_lesson_id))
        
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)

        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        

                
    def test_page__post_preview__item__navigate_to_whiteboard(self):
        # setup

        # reveal schedule list
        elem = self.test_context.find_element_by_id('ctl-lesson_schedudle--{}'.format(self.test_lesson_id))
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.click()

        self.wait(s=1)

        # open whiteboard 

        elem = self.test_context.find_element_by_id('lnk-whiteboard_view--{}'.format(self.test_lesson_schedule_id))
        
        self.wait(s=2)

        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')
        

