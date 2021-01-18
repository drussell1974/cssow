from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_lessonkeyword_edit_not_found(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        pass

    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """

    def test_page_should_redirect_to_404__if_scheme_of_work_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/keywords/{}/edit".format(999999, self.test_lesson_id, self.test_keyword_id))

        # assert
        #self.assertCustom404("item (220, 999999) does not exist, is currently unavailable or you do not have permission.")
        self.assertCustomPermissionDenied(h1="PermissionError at /schemesofwork/999999/lessons/220/keywords/92/edit")


    def test_page_should_redirect_to_404__if_lesson_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/keywords/{}/edit".format(self.test_scheme_of_work_id, 999999, self.test_keyword_id))

        # assert
        self.assertCustom404("item (999999, 11) does not exist, is currently unavailable or you do not have permission.")


    def test_page_should_redirect_to_404__if_keyword_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/keywords/{}/edit".format(self.test_scheme_of_work_id, self.test_lesson_id, 999999))

        # assert
        self.assertCustom404("(id=0) (999999, 220, 11) does not exist, is currently unavailable or you do not have permission.")


    @skip("Add lesson_id to stored keyword__get or an alternative to get lessons for keyword")
    def test_page_should_redirect_to_404__if_keyword_id__is_not_part_of_lesson(self):
        # act
        self.do_log_in(self.root_uri + "/schemesofwork/{}/lessons/{}/keywords/{}/edit".format(self.test_scheme_of_work_id, 131, self.test_keyword_id))

        # assert
        self.assertCustom404("item (131, 11) does not exist, is currently unavailable or you do not have permission.")
