from datetime import datetime
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_schemesofwork_edit_existing(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.try_log_in("http://dev.computersciencesow.net:8000/schemeofwork/schemesofwork/edit?id={}&_next=%2Fschemeofwork%2Fschemesofwork%2Findex".format(self.test_scheme_of_work_id))


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    """ Check content """

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        """ Check content """
        # setup
        #self.do_log_in(redirect_to_uri_on_login="http://dev.computersciencesow.net:8000/schemeofwork/schemesofwork/edit?id={}&_next=%2Fschemeofwork%2Fschemesofwork%2Findex".format(self.test_scheme_of_work_id))

        # test
        save = self.test_context.find_element_by_id('saveButton')
        saveandpublish = self.test_context.find_element_by_id('saveAndPublishButton')

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'KS5 OCR')
        self.assertEqual("DRAFT", save.text)
        self.assertEqual("SAVE AND PUBLISH", saveandpublish.text)


    """ navigation """

    def test_page__breadcrumb_navigate_to_learning_episode_index(self):
        # test
        elem = self.test_context.find_element_by_id('lnk-bc-learning_episodes')

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'A-Level Computer Science')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-schemes_of_work')
        self.assertEqual("Schemes of Work", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__breadcrumb__navigate_to_learningepisode_index(self):
        # setup
        elem = self.test_context.find_element_by_id('lnk-bc-learning_episodes')
        self.assertEqual("Lessons", elem.text)

        # test
        elem.click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Lessons', 'A-Level Computer Science')


    """ editing """


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

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'KS5 OCR')


    def test_page__edit_existing__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-description")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Fill in field with some information '
        elem.clear()
        elem.send_keys("test_page__edit_existing__should_redirect_to_index_if_valid, last updated this field {}".format(datetime.now()))

        ' select the submit button (to remove cursor from textarea '

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')





