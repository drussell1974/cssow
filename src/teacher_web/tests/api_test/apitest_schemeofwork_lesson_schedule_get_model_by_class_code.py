from django.test import tag
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_lesson_schedule_get_model_by_class_code(APITestCase):


    def setUp(self):
        # set up
        
        test_class_code = "FTRXZQ"

        self.get(f"/api/schedule/lesson/{test_class_code}")
        

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
        self.assertEqual(15, self.payload["schedule"]["id"])

 
    def test__should_have_lesson_id(self):
        # assert
        self.assertEqual(220, self.payload["schedule"]["lesson_id"])


    def test__should_have_scheme_of_work_id(self):
        # assert
        self.assertEqual(11, self.payload["schedule"]["scheme_of_work_id"])


    def test__should_have_department_id(self):
        # assert
        self.assertEqual(5, self.payload["schedule"]["department_id"])


    def test__should_have_institute_id(self):
        # assert
        self.assertEqual(2, self.payload["schedule"]["institute_id"])
