from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.support.select import Select

class uitest_schemeofwork_content_index_not_found(UITestCase):

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
        self.do_log_in(self.root_uri + "/schemesofwork/{}/curriculum-content".format(999999))

        # assert
        self.assertCustomPermissionDenied(h1="PermissionError at /schemesofwork/999999/curriculum-content/")
        #self.assertCustom404("(id=0) (999999,) does not exist, is currrently unavailable or you do not have permission.")
