from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_learningobjective_edit_not_found(UITestCase):

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
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{99999999}/lessons/{self.test_lesson_id}/learning-objectives/{self.test_learning_objective_id}/edit")

        # assert
        self.assertCustom404("The item is currently unavailable or you do not have permission.")


    def test_page_should_redirect_to_404__if_lesson_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{99999999}/learning-objectives/{self.test_learning_objective_id}/edit")

        # assert
        self.assertCustom404("The item is currently unavailable or you do not have permission.")


    def test_page_should_redirect_to_404__if_resource_id__does_not_exist(self):
        # act        
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/learning-objectives/{999999999}/edit")

        # assert
        self.assertCustom404("The item is currently unavailable or you do not have permission.")
        