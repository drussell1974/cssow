from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_schemesofwork_edit_create_new(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/schemesofwork/edit")


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

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/edit/new')


    def test_page__breadcrumb__navigate_to_default_index(self):
        #test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[1]/a')
        self.assertEqual("Home", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('default/index')


    def test_page__breadcrumb_navigate_to_learning_episode_index_not_visible_for_new_schemeofwork(self):
        # test and assert
        with self.assertRaises(Exception):
            self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[3]/a')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[2]/a')
        self.assertEqual("Schemes of work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/index')


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
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/edit/new')


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
        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning episodes', 'for should_redirect_to_index_if_valid')




