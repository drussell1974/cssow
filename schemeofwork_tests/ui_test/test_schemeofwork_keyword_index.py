from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_keyword_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://dev.computersciencesow.net:8000/keyword")
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


    def test_page__should_show__keywords_page_1(self):
        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertEqual(10, len(elems))


    def test_page__should_show__keywords_page_2(self):
        # setup
        page2 = self.test_context.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/ul/li[2]/a")
        self.test_context.implicitly_wait(20)
        page2.click()

        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertEqual(10, len(elems))



