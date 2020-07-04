from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class test_schemeofwork_resources_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.test_context.implicitly_wait(10)
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/resources/new".format(self.test_scheme_of_work_id, self.test_lesson_id))


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
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','Types of CPU architecture','New')


    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        self.test_context.implicitly_wait(10)
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # test

        ' Create valid information '

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' ctl-uri '
        elem = self.test_context.find_element_by_id("ctl-uri")
        elem.send_keys("https://www.pgonline.co.uk/resources/computer-science/a-level-ocr/ocr-a-level-textbook/")

        ' ctl-publisher '
        elem = self.test_context.find_element_by_id("ctl-publisher")
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-type_id '
        elem = Select(self.test_context.find_element_by_id("ctl-type_id"))
        elem.select_by_visible_text("Book")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)
        self.wait(s=1)

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture\; CISC and RISC')

        # delete

        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()