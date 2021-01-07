import json
from django.test import tag
from api_testcase import APITestCase

class apitest_schemeofwork_resource_get_markdown(APITestCase):


    def setUp(self):
        # set up
        #TODO: #254 get ids from settings 
        uri = "/api/schemesofwork/{}/lessons/{}/resources/{}/markdown/{}?format=json".format(self.test_scheme_of_work_id, self.test_lesson_id, self.test_md_document_resource_id, self.test_md_document_name)
        self.get(uri)
        
    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    @tag("markdown should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["markdown"])


    def test__first_should_have_name(self):
        # check first few characters
        self.assertEqual('<h1>consectetur adipisci', self.payload["markdown"][0:24])
