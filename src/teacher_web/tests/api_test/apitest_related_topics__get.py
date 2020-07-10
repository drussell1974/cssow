import json
from django.test import tag
from api_testcase import APITestCase


class apitest_related_topics__get(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/related-topics/2")
        
        self.last_item_index = len(self.payload["related-topics"]) - 1


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["related-topics"])


    def test__should_return_list_of_topics(self):
        self.assertEqual(42, self.payload["related-topics"][0]["id"])
        self.assertEqual("Operators", self.payload["related-topics"][0]["name"])

        self.assertEqual(57, self.payload["related-topics"][self.last_item_index]["id"])
        self.assertEqual("Run-time environment", self.payload["related-topics"][self.last_item_index]["name"])
        