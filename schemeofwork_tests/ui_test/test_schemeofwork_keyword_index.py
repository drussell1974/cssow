from ui_testcase import UITestCase, WebBrowserContext

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
        elem.send_keys("algorithm")
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

