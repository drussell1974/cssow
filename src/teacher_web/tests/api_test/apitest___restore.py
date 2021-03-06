import json
from unittest import skip
from django.test import tag
from api_testcase import APITestCase


class apitest___restore(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/demo/restore-data")
        

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload["complete"])
