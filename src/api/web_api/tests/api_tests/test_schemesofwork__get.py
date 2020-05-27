import json

from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
#from django.urls import reverse
        
#from lessons.views import get

@tag("schemeofwork")
class test_schemeofwork__get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://localhost:8000/api/schemeofwork")
        self.test_context.implicitly_wait(4)

        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        
        self.payload = json.loads(content)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """def test__should_resolve_url(self):
        found = reverse("schemesofwork")
        self.assertEqual(found,"/api/schemeofwork")"""

    @tag("schemeofwork should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["schemesofwork"])