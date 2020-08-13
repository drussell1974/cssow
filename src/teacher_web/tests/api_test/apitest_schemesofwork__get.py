import json
from django.test import tag
from api_testcase import APITestCase

class apitest_schemeofwork__get(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/schemesofwork")


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    @tag("schemeofwork should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["schemesofwork"])


    def test__first_should_have_name(self):
        self.assertEqual('KS3 Computing', self.payload["schemesofwork"][0]["name"])


    def test__first_should_have_desription(self):
        self.assertEqual('Lorem ipsum dolor sit amet.', self.payload["schemesofwork"][0]["description"].rstrip())


    def test__last_should_have_name(self):
        self.assertEqual('A-Level Computer Science', self.payload["schemesofwork"][2]["name"])


    def test__last_should_have_desription(self):
        self.assertEqual('Computing curriculum for A-Level', self.payload["schemesofwork"][2]["description"].rstrip())

