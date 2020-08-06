from unittest import TestCase
from shared.models.core.helper_string import dictionary_to_string

class test__helper_string__dictionary_to_string_without_filter(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_return_error_as_empty_string(self):
        # test
        self.assertRaises(Exception, dictionary_to_string([], "foo"))


    def test_return_single_item_first_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar"}], "foo")

        #assert
        self.assertEqual("bar", result)


    def test_return_multiple_items_first_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar"},{"foo":"ray"}], "foo")

        #assert
        self.assertEqual("bar, ray", result)


    def test_return_multiple_items_nth_key(self):
        # test
        result = dictionary_to_string([{"foo":"bar","score":10},{"foo":"ray","score":8}], "score")

        #assert
        self.assertEqual("10, 8", result)





