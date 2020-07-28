from django.test import tag
from api_testcase import APITestCase
from django.urls import reverse

class apitest_schemeofwork_lesson_get_model__filter(APITestCase):

    def setUp(self):
        # set up
        pass


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        pass


    def show_payload(self, filter_by_resource_type_id):
        self.get("/api/schemesofwork/{}/lessons/{}?resource_type_id={}".format(self.test_scheme_of_work_id, self.test_lesson_id, filter_by_resource_type_id))
        

    def test__should_show_all_resources_when_zero(self):
        # arrange
        self.show_payload(filter_by_resource_type_id=0)
        
        # assert
        self.assertEqual(4, len(self.payload["lesson"]["resources"]))
        
        
    def test__should_have_resources__books(self):
        # arrange
        self.show_payload(filter_by_resource_type_id=6)

        # assert
        self.assertEqual(2, len(self.payload["lesson"]["resources"]))
        