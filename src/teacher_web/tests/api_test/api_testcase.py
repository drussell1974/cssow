from django.db import connection as db
from unittest import TestCase
import json
import os
import requests

class APITestCase(TestCase):

    root_uri = os.environ["TEST_URI"]
    test_scheme_of_work_id = os.environ["TEST_SCHEME_OF_WORK_ID"]
    test_lesson_id = os.environ["TEST_LESSON_ID"] 
    test_learning_objective_id = os.environ["TEST_LEARNING_OBJECTIVE_ID"]
    test_reference = os.environ["TEST_RESOURCE_ID"]
    test_md_document_resource_id = os.environ["TEST_MD_DOCUMENT_RESOURCE_ID"]
    test_md_document_name = os.environ["TEST_MD_DOCUMENT_NAME"]
    
    def wait(self, s = 5):
        import time
        time.sleep(s)

    def get(self, uri):
        full_uri = self.root_uri + uri
        self.test_context = requests.get(full_uri)
        self.payload = json.loads( self.test_context.content)