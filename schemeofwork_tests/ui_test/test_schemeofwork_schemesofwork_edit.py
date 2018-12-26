from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_schemesofwork_edit(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/schemesofwork/edit?id=76")


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_have__title__title_heading__and__sub_heading(self):

        # test

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/edit')


    def test_page__breadcrumb_navigate_to_learning_episode_index(self):
        # test
        elem = self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[3]/a')

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

        ' sleep to give time for browser to respond '
        import time
        time.sleep(3)

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/index')


    def test_page__breadcrumb__navigate_to_default_index(self):
        #test
        self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[1]/a').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('default/index')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # test
        self.test_context.find_element_by_xpath('//*[@id="itemNav"]/div/ul/li[2]/a').click()

        # assert
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/index')


    def test_page__edit_existing__should_stay_on_same_page_if_invalid(self):
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

        ' sleep to give time to ensure browser HAS not redirected '
        import time
        time.sleep(3)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadingsByRoute('schemesofwork/edit')


    def test_page__edit_existing__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-description")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Fill in field as blank '
        elem.clear()
        elem.send_keys("test_page__edit_existing__should_redirect_to_index_if_valid" + str(datetime.now()))

        ' select the submit button (to remove cursor from  textarea '
        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        ' sleep to give time to ensure browser has redirected '
        import time
        time.sleep(3)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadingsByRoute('learningepisode/index')





