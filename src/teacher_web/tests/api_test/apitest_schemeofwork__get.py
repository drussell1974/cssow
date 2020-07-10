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
