import json
from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork__get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/api/schemesofwork/{}".format(self.test_scheme_of_work_id))
        self.test_context.implicitly_wait(4)

        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        
        self.payload = json.loads(content)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["schemeofwork"])


    def test__should_have_name(self):
        self.assertEqual('A-Level Computer Science', self.payload["schemeofwork"]["name"])


    def test__should_have_desription(self):
        self.assertEqual('Computing curriculum for A-Level', self.payload["schemeofwork"]["description"].rstrip())