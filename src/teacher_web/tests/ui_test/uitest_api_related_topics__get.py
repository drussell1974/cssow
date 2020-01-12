import json
from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext


class uitest_api_related_topics__get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/api/related-topics/2")
        self.test_context.implicitly_wait(4)

        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        
        self.payload = json.loads(content)
        self.last_item_index = len(self.payload["related-topics"]) - 1


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["related-topics"])


    def test__should_return_list_of_topics(self):
        self.assertEqual(42, self.payload["related-topics"][0]["id"])
        self.assertEqual("Operators", self.payload["related-topics"][0]["name"])

        self.assertEqual(57, self.payload["related-topics"][self.last_item_index]["id"])
        self.assertEqual("Run-time environment", self.payload["related-topics"][self.last_item_index]["name"])
        