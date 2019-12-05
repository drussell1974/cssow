from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from helper_sort_and_search import sort_array

class test__helper_string__merge_stringlist(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__return_empty(self):
        # setup

        # test
        result = sort_array([])

        # assert
        self.assertEqual([], result)


    def test__return_two_sorted_items(self):
        # setup

        # test
        result = sort_array(["A", "B"])

        # assert
        self.assertEqual(["A", "B"], result)


    def test__return_three_sorted_items(self):
        # setup

        # test
        result = sort_array(["A", "B", "C"])

        # assert
        self.assertEqual(["A", "B", "C"], result)


    def test__return_two_unsorted_items(self):
        # setup

        # test
        result = sort_array(["C", "B"])

        # assert
        self.assertEqual(["B", "C"], result)


    def test__return_three_unsorted_items(self):
        # setup

        # test
        result = sort_array(["C", "A", "B"])

        # assert
        self.assertEqual(["A", "B", "C"], result)


    def test_return_assorted_mixed_items(self):
        # setup
        unsorted_array = ["cascading style sheets (css)",
                        "embedded css",
                        "form controls",
                        "html classes",
                        "html identifiers",
                        "html tags",
                        "inline css",
                        "javascript",
                        "web forms",
                        "external css",
                        "html",
                        "hyper text markup language (html)"]

        # test
        result = sort_array(unsorted_array)

        # assert
        expected = ["cascading style sheets (css)",
                        "embedded css",
                        "external css",
                        "form controls",
                        "html",
                        "html classes",
                        "html identifiers",
                        "html tags",
                        "hyper text markup language (html)",
                        "inline css",
                        "javascript",
                        "web forms"]

        self.assertEqual(expected, result)


    def test_return_assorted_mixed_items_2(self):
        # setup
        unsorted_array = ["", "Cache",
                        "Random Access Memory (Ram)",
                        "Read Only Memory (Rom)",
                        "Flash Storage",
                        "Virtual Memory"]

        # test
        result = sort_array(unsorted_array)

        # assert
        expected = ["", "Cache",
                        "Flash Storage",
                        "Random Access Memory (Ram)",
                        "Read Only Memory (Rom)",
                        "Virtual Memory"]

        self.assertEqual(expected, result)
