from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_content_edit_not_found(UITestCase):

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

    def test_page_should_redirect_to_LoginPage__if_scheme_of_work_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{}/curriculum-content/{}/edit".format(999999, self.test_content_id))

        # assert
        self.assertLoginPage(login_message="The item is currently unavailable or you do not have permission.")


    def test_page_should_redirect_to_404__if_lesson_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{}/curriculum-content/{}/edit".format(self.test_scheme_of_work_id, 999999))

        # assert
        self.assertCustom404("A-Level Computer Science (id=11) (999999, 11) does not exist, is currently unavailable or you do not have permission.")

