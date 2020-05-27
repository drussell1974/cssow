from datetime import datetime
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_schemesofwork_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/schemesofwork/edit")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):
        """ Heading blank """
        # test
        save = self.test_context.find_element_by_id('saveButton')
        saveandpublish = self.test_context.find_element_by_id('saveAndPublishButton')

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Scheme of Work', 'Create a new scheme of work')
        self.assertEqual("DRAFT", save.text)
        self.assertEqual("SAVE AND PUBLISH", saveandpublish.text)


    def test_page__breadcrumb_navigate_to_lesson_index_not_visible_for_new_schemeofwork(self):
        # test and assert
        with self.assertRaises(Exception):
            self.test_context.find_element_by_id('lnk-bc-learning_episoodes')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # test
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("Schemes of Work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    """ edit """


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-name")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Fill in field as blank '
        elem.clear()
        elem.send_keys("")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Scheme of Work', 'Create a new scheme of work')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-description")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' name '
        elem = self.test_context.find_element_by_id("ctl-name")
        elem.send_keys("should_redirect_to_index_if_valid")

        ' exam board - just skip as not required'
        elem = self.test_context.find_element_by_id("ctl-exam_board_id")
        elem.send_keys(Keys.TAB)

        ' key stage - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-key_stage_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "KS4":
                 opt.click()

        elem.send_keys(Keys.TAB)

        ' description - Fill in field with some information '
        elem.send_keys("test_schemeofwork_schemesofwork_new.test_page__edit_existing__should_redirect_to_index_if_valid, last updated this field {}" + str(datetime.now()))

        ' select the submit button (to remove cursor from textarea '

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'should_redirect_to_index_if_valid')




