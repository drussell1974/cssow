from django.test import tag
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_lesson_get_model(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/institute/{}/department/{}/schemesofwork/{}/lessons/{}".format(self.test_institute_id, self.test_department_id, self.test_scheme_of_work_id, self.test_lesson_id))
        

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        
    
    def test__should_have_id(self):
        # assert
        self.assertEqual(220, self.payload["lesson"]["id"])


    def test__should_have_title(self):
        # assert
        self.assertEqual('Types of CPU architecture', self.payload["lesson"]["title"])

        
    def test__should_have_summary(self):
        # assert
        self.assertEqual('Von Neumann architecture and Harvard architecture, and CISC and RISC', self.payload["lesson"]["summary"])


    def test__should_have_lesson_objectives(self):
        # assert
        self.assertEqual(8, len(self.payload["lesson"]["learning_objectives"]))


    def test__should_have_resources(self):
        # assert
        self.assertEqual(4, len(self.payload["lesson"]["resources"]))


    def test__should_have_key_words(self):
        # assert
        self.assertEqual(3, len(self.payload["lesson"]["key_words"]))


    def test__should_have_missing_words_challenge(self):
        # assert
        self.assertEqual("", self.payload["lesson"]["learning_objectives"][7]["missing_words_challenge"])
