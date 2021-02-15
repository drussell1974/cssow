import json
from django.test import tag
from api_testcase import APITestCase

class apitest_schemeofwork_lesson_resource_get_markdown(APITestCase):


    def setUp(self):
        # set up
        #TODO: #254 get ids from settings 
        uri = f"/api/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/{self.test_md_document_resource_id}/markdown/{self.test_md_document_name}?format=json"
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
        self.assertEqual('<h1>Configure DHCP on a ', self.payload["markdown"][0:24])
