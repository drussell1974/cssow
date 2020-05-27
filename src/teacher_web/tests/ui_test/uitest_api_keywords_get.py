import json
from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext


class uitest_api_keywords_get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/api/keywords")
        self.test_context.implicitly_wait(4)

        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        
        self.payload = json.loads(content)
        self.last_item_index = len(self.payload["keywords"]) - 1


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["keywords"])


    def test__should_be_alphabetical_order(self):
        self.assertEqual([335,'3D printer'], self.payload["keywords"][0])
        self.assertEqual([241,'XOR expression'], self.payload["keywords"][self.last_item_index])