from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse

class uitest_api_schemeofwork_lesson_get_model__filter(UITestCase):

    def show_payload(self, filter_by_resource_type_id):

        self.test_context.get(self.root_uri + "/api/schemesofwork/{}/lessons/{}?resource_type_id={}".format(self.test_scheme_of_work_id, self.test_lesson_id, filter_by_resource_type_id))
        self.test_context.implicitly_wait(4)
        
        # act
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        import json
        self.payload = json.loads(content)


    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test__should_show_all_resources_when_zero(self):
        # arrange
        self.show_payload(filter_by_resource_type_id=0)
        
        # assert
        self.assertEqual(3, len(self.payload["lesson"]["resources"]))
        
        
    def test__should_have_resources__books(self):
        # arrange
        self.show_payload(filter_by_resource_type_id=6)

        # assert
        self.assertEqual(1, len(self.payload["lesson"]["resources"]))
        