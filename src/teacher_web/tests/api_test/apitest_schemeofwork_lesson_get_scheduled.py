from django.test import tag
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_lessons_scheduled_get_model(APITestCase):


    def setUp(self):
        # set up
        self.get("/api/institute/{}/schedule".format(self.test_institute_id))
        

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
        self.assertEqual('The CPU', self.payload["schedule"][0]["title"])


    def test__should_have_lesson_id(self):
        # assert
        self.assertEqual(131, self.payload["schedule"][0]["lesson_id"])


    def test__should_have_datetime(self):
        # assert
        self.assertEqual("2021-04-03T11:53:00", self.payload["schedule"][0]["start_date"])
