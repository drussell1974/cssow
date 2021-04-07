import json
from unittest import skip 
from django.test import tag
from api_testcase import APITestCase

class apitest_notification__get(APITestCase):


    def setUp(self):
        # set up
        self.get(f"/api/notifications/0/delete")


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["result"])


    @skip("implement log in")
    def test__first_should_have_id(self):
        self.assertEqual('', self.payload["result"][0]["id"])


    @skip("implement log in")
    def test__first_should_have_message(self):
        self.assertEqual('', self.payload["messages"][0]["message"].rstrip())


    @skip("implement log in")
    def test__first_should_have_action(self):
        self.assertEqual('', self.payload["messages"][0]["action"].rstrip())


    @skip("implement log in")
    def test__last_should_have_id(self):
        self.assertEqual('', self.payload["messages"][2]["id"])


    @skip("implement log in")
    def test__last_should_have_message(self):
        self.assertEqual('', self.payload["messages"][2]["message"].rstrip())


    @skip("implement log in")
    def test__last_should_have_action(self):
        self.assertEqual('', self.payload["messages"][2]["action"].rstrip())
