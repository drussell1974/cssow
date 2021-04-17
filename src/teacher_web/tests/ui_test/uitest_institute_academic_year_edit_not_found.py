from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_institute_academic_year_edit_not_found(UITestCase):

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

    def test_page_should_redirect_to_login_page__if_scheme_of_work_id__does_not_exist(self):
        # act        
        self.do_log_in(f"/institute/{self.test_institute_id}/academic-years/{9999999}/edit")

        # assert
        self.assertCustom404("The item is currently unavailable or you do not have permission.")


    def test_page_should_redirect_to_404__if_institute_id__does_not_exist(self):
        # act        
        self.do_log_in(f"/institute/{999999}/academic-years/{2020}/edit")
        # assert
        self.assertCustom404("The item is currently unavailable or you do not have permission.")
