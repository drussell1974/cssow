from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_keyword_new(UITestCase):

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


    def test_page__should_show__keywords_page_2(self):
        # setup
        page2 = self.test_context.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/ul/li[2]/a")
        self.test_context.implicitly_wait(20)
        page2.click()

        # test
        elems = self.test_context.find_elements_by_class_name("card")

        # assert
        self.assertEqual(10, len(elems))



