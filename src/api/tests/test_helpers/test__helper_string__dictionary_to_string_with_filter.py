from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from helper_string import dictionary_to_string

class test__helper_string__dictionary_to_string_with_filter(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_return_error_as_empty_string(self):
        # test
        self.assertRaises(Exception, dictionary_to_string([], "foo"), {"foo":"bar"})


    def test_return_single_item_first_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar"}], "foo",  {"foo":"bar"})

        #assert
        self.assertEqual("bar", result)


    def test_return_multiple_items_first_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar"},{"foo":"do"},{"foo":"ray"}], "foo",  {"foo":"bar"})

        #assert
        self.assertEqual("bar", result)


    def test_return_multiple_items_second_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar","score":10},{"foo":"ray","score":8},{"foo":"do","score":10}], "foo",  {"score":10})

        #assert
        self.assertEqual("bar, do", result)





