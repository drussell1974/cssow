from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepisode_edit_existing(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.test_context.implicitly_wait(10)
        self.do_log_in("http://dev.computersciencesow.net:8000/schemeofwork/learningobjective/index/{}/{}".format(self.test_scheme_of_work_id, self.test_learning_episode_id))

        ' click the add reference button '
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_id("edit-reference-{}".format(self.test_reference))
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        elem.click()


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """


    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-title - leave EMPTY '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys(Keys.TAB)


        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Reference','ocr as and a level computer science from pg online limited for a-level computer science')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys("OCR AS and A Level Computer Science")

        ' ctl-year_published '
        elem = self.test_context.find_element_by_id("ctl-year_published")
        elem.clear()
        elem.send_keys("2016")

        ' ctl-authors '
        elem = self.test_context.find_element_by_id("ctl-authors")
        elem.clear()
        elem.send_keys("Heathcoate, P. M.; Heathcoate, R. S. U.")

        ' ctl-publisher '
        elem = self.test_context.find_element_by_id("ctl-publisher")
        elem.clear()
        elem.send_keys("PG Online Limited")

        ' ctl-uri '
        elem = self.test_context.find_element_by_id("ctl-uri")
        elem.clear()
        elem.send_keys("https://www.pgonline.co.uk/resources/computer-science/a-level-ocr/ocr-a-level-textbook/")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork','Learning Objectives','for a-level computer science - week 1 - programming and development')
