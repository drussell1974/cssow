from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_lessonkeyword_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # arrange

        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/new")

        # create content
        
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys("Lorem ipsum DEL 220")

        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.send_keys("test page  redirect to index if valid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')


    def tearDown(self):
        
        elem = self.find_element_by_id__with_explicit_wait("btn-delete-unpublished", wait=2)
        ' Ensure element is visible '
        # TODO: #323 add scrolllIntoView() to find_element_by_id__with_explicit_wait
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)

        elem.click()

        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_redirect_to_index_after_deletion(self):

        #delete
        ' Open edit '
        self.delete_unpublished_item(".unpublished a.edit .fa-edit")
        
        self.wait(s=3)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')
        
        #231: items after should be less than before
        
        items_after = self.test_context.find_elements_by_class_name("card-keyword")
        self.assertEqual(3, len(items_after))

