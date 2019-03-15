from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.common.keys import Keys

class test_schemeofwork_keyword_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in("http://dev.computersciencesow.net:8000/keyword")
        self.test_context.implicitly_wait(4)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Key terms and definitions', 'Key terms and their definitions for all key stages')


    def test_page__should_show__all_keywords(self):
        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertTrue(len(elems) > 0)


    def test_page__should_show__one_filtered_keywords(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-search")
        elem.send_keys("algorith")
        elem.send_keys("m")
        elem.send_keys(Keys.TAB)
        self.wait() # do not remove

        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertEqual(1, len(elems))


    def test_page__should_show__multiple_filtered_keywords(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-search")
        elem.send_keys("abstract,")
        elem.send_keys("algorithm")
        self.wait() # do not remove

        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertEqual(2, len(elems))


    def test_update_definition(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-search")
        elem.send_keys("algorith")
        elem.send_keys("m")
        elem.send_keys(Keys.TAB)
        self.wait(30) # do not remove

        # test
        elem_text348 = self.test_context.find_element_by_id("ctl-definition-348")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem_text348)

        elem_text348.clear()
        elem_text348.send_keys('Step-by-step instructions designed to solve a problem.')

        elem_save348 = self.test_context.find_element_by_id("save348")
        elem_save348.click()

        self.wait() # do not remove

        msg348 = self.test_context.find_element_by_id("message348")
        err348 = self.test_context.find_element_by_id("error348")

        # assert
        self.assertEqual("updated", msg348.text, "Success message not as expected")
        self.assertEqual("", err348.text, "Error message not as expected")


    def test_revert_definition(self):
        # setup
        elem = self.test_context.find_element_by_id("ctl-search")
        elem.send_keys("algorithm")
        self.wait() # do not remove

        # test
        elem_text348 = self.test_context.find_element_by_id("ctl-definition-348")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem_text348)

        elem_text348.clear()
        elem_text348.send_keys('Step-by-step instructiondfdasfsas designed to solve a problem.')

        elem_save348 = self.test_context.find_element_by_id("cancel348")
        elem_save348.click()

        self.wait() # do not remove

        msg348 = self.test_context.find_element_by_id("message348")
        err348 = self.test_context.find_element_by_id("error348")

        # assert
        self.assertEqual("reverted", msg348.text, "Success message not as expected")
        self.assertEqual("", err348.text, "Error message not as expected")
        self.assertEqual("Step-by-step instructions designed to solve a problem.", elem_text348.text, "Text has not been reverted")
