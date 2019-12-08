from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse
#from lessons.views import get

class test_schemeofwork_learningepsiode_get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://localhost:8000/api/schemeofwork/{}/lessons".format(self.test_scheme_of_work_id))
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test__should_resolve_url(self):
        found = reverse("lessons")
        self.assertEqual(found, "/api/schemeofwork/11/lessons")


    def test__should_return_a_payload(self):
        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        import json
        payload = json.loads(content)
        
        # act
        
        # assert
        self.assertIsNone(payload)
