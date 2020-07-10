import json
from django.test import tag
from api_testcase import APITestCase


class apitest_keywords_get(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/keywords")
        
        self.last_item_index = len(self.payload["keywords"]) - 1


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["keywords"])


    def test__should_be_alphabetical_order(self):
        self.assertEqual([335,'3D printer'], self.payload["keywords"][0])
        self.assertEqual([241,'XOR expression'], self.payload["keywords"][self.last_item_index])