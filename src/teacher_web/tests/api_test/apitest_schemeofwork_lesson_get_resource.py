from django.test import tag
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_resource_get_model(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/schemesofwork/{}/lessons/{}/resources/{}".format(self.test_scheme_of_work_id, self.test_lesson_id, self.test_reference))
        

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        
    
    def test__should_have_title(self):
        # assert
        self.assertEqual('OCR AS and A Level Computer Science', self.payload["resource"]["title"])

    
    def test__should_have_publisher(self):
        # assert
        self.assertEqual('PM Heathcote and RSU Heathcote, PG Online, 2016', self.payload["resource"]["publisher"])


    def test__should_have_page_note(self):
        # assert
        self.assertEqual('The TCP/IP Protocol Stack - pages 122 - 123', self.payload["resource"]["page_note"])


    def test__should_have_page_uri(self):
        # assert
        self.assertEqual('', self.payload["resource"]["page_uri"])


    def test__should_have_md_document_name(self):
        # assert
        self.assertEqual('', self.payload["resource"]["md_document_name"])


    def test__should_have_type_id(self):
        # assert
        self.assertEqual(6, self.payload["resource"]["type_id"])


    def test__should_have_type_name(self):
        # assert
        self.assertEqual('Book', self.payload["resource"]["type_name"])


    def test__should_have_lesson_id(self):
        # assert
        self.assertEqual(220, self.payload["resource"]["lesson_id"])

