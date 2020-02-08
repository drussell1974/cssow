from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse

class uitest_schemeofwork_lesson_get_model(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/api/schemesofwork/{}/lessons/{}".format(self.test_scheme_of_work_id, self.test_lesson_id))
        self.test_context.implicitly_wait(4)
        
        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        import json
        self.payload = json.loads(content)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


#    def test__should_resolve_url(self):
#        found = reverse("lessons")
#        self.assertEqual(found, "/api/schemeofwork/11/lessons")


    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        
    
    def test__should_have_title(self):
        # assert
        self.assertEqual('Types of CPU architecture', self.payload["lesson"]["title"])

        
    def test__should_have_summary(self):
        # assert
        self.assertEqual('Von Neumann architecture and Harvard architecture\; CISC and RISC', self.payload["lesson"]["summary"])


    def test__should_have_lesson_objectives(self):
        # assert
        self.assertEqual(8, len(self.payload["lesson"]["learning_objectives"]))


    def test__should_have_resources(self):
        # assert
        self.assertEqual(3, len(self.payload["lesson"]["resources"]))
        