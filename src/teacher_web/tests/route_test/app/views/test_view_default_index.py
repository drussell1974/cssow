from unittest import TestCase, skip
from django.test import Client
from django.test.utils import setup_test_environment, teardown_test_environment


# test context

class test_view_default_index(TestCase):

    def setUp(self):
        teardown_test_environment()
        setup_test_environment()

    def tearDown(self):
        # end test
        
    @skip("not tested")
    def test_index_should_return_default(self):
        self.assertEqual(1,1)