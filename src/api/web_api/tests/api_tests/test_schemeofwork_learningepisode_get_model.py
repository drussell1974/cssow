from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse
#from lessons.views import get

@tag("learningepisode")
class test_schemeofwork_learningepsiode_get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get("http://localhost:8000/api/schemeofwork/{}/lessons/{}".format(self.test_scheme_of_work_id, self.test_learning_episode_id))
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


    @tag("learningepisode should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        
    
    @tag("learningepisode should have title")
    def test__should_have_title(self):
        # assert
        self.assertEqual('The CPU', self.payload["lesson"]["title"])

        
    @tag("learningepisode should have summary")
    def test__should_have_summary(self):
        # assert
        self.assertEqual('CPU components: ALU, Control Unit, Registers and Buses', self.payload["lesson"]["summary"])

    @tag("learningepisode should have lesson objectives")
    def test__should_have_lesson_objectives(self):
        # assert
        self.assertEquals(9, len(self.payload["lesson"]["learning_objectives"]))


    @tag("learningepisode should have resources")
    def test__should_have_resources(self):
        # assert
        self.assertEquals(14, len(self.payload["lesson"]["resources"]))
        