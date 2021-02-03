from django.test import tag
from api_testcase import APITestCase

import requests

class apitest_schemeofwork__get(APITestCase):

    
    def setUp(self):
        # set up

        self.get("/api/schemesofwork/{}".format(self.test_scheme_of_work_id))

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["schemeofwork"])


    def test__should_have_name(self):
        #self.assertEqual('A-Level Computer Science', self.payload[0:49])
        self.assertEqual('A-Level Computer Science', self.payload["schemeofwork"]["name"])


    def test__should_have_desription(self):
        self.assertEqual('Computing curriculum for A-Level', self.payload["schemeofwork"]["description"].rstrip())


    def test__should_have_number_of_resources(self):
        self.assertEqual(60, self.payload["schemeofwork"]["number_of_resources"])


    def test__should_have_number_of_lessons(self):
        self.assertEqual(25, self.payload["schemeofwork"]["number_of_lessons"])


    def test__should_have_number_of_learning_objectives(self):
        self.assertEqual(127, self.payload["schemeofwork"]["number_of_learning_objectives"])


    def test__should_have_keywords(self):
        self.assertEqual(155, self.payload["schemeofwork"]["number_of_keywords"])
