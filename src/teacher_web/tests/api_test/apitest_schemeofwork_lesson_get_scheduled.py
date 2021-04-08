from django.test import tag
from unittest import skip
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_lessons_scheduled_get_model(APITestCase):


    def setUp(self):
        # set up
        url = "/api/schedule/institute/{}/department/{}/schemesofwork/{}/lessons/{}/events".format(self.test_institute_id, self.test_department_id, self.test_scheme_of_work_id, self.test_lesson_id)
        self.get(url)
        

    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertEqual([], self.payload["schedule"])


    @skip("not guarenteed")
    def test__should_have_title(self):
        # assert
        self.assertEqual('The CPU', self.payload["schedule"][0]["title"])


    @skip("not guarenteed")
    def test__should_have_lesson_id(self):
        # assert
        self.assertEqual(131, self.payload["schedule"][0]["lesson_id"])


    @skip("not guarenteed")
    def test__should_have_datetime(self):
        # assert
        self.assertEqual("2021-04-03T11:53:00", self.payload["schedule"][0]["start_date"])
