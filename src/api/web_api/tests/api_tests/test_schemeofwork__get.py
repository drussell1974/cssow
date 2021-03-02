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
        self.do_get("http://localhost:8000/api/schemeofwork/{}".format(self.test_scheme_of_work_id), wait=2)

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
        found = reverse("schemeofwork")
        self.assertEqual(found,"/api/schemeofwork/11")"""

    @tag("schemeofwork should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        self.assertIsNotNone(self.payload["schemeofwork"])

    @tag("schemeofwork should have name")
    def test__should_have_name(self):
        self.assertEqual('A-Level Computer Science', self.payload["schemeofwork"]["name"])


    @tag("schemeofwork should have description")
    def test__should_have_desription(self):
        self.assertEqual('Computing curriculum for A-Level', self.payload["schemeofwork"]["description"].rstrip())