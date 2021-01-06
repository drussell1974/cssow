from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_schemesofworkkeyword_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        #self.test_context.implicitly_wait(10)
        
        # setup

        self.do_log_in(self.root_uri + "/schemesofwork/{}/keywords/new".format(self.test_scheme_of_work_id))

        # create content
        
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys("Lorem ipsum DEL 11")

        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.send_keys("test page  redirect to index if valid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=5)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')



    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_redirect_to_index_after_deletion(self):

        #delete

        ' Open edit '
        self.delete_unpublished_item(".unpublished h5.card-title")
        
        self.wait(s=2)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')
        
        #231: items after should be less than before
        
        items_after = self.test_context.find_elements_by_class_name("card-keyword")
        self.assertEqual(155, len(items_after))