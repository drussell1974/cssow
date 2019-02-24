from unittest import TestCase

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from helper_string import to_cs_string

class test__helper_string__to_cs_string(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__return_empty_when_items_are_empty(self):
        # setup

        # test
        result = to_cs_string("", "", "")

        # assert
        self.assertEqual("", result)


    def test__return_empty_when_items_are_none(self):
        # setup

        # test
        result = to_cs_string(None, None, None)

        # assert
        self.assertEqual("", result)


    def test__return_single_item_if_item2_is_empty(self):
        # setup

        # test
        result = to_cs_string("item1", "")

        # assert
        self.assertEqual("item1", result)


    def test__return_single_item_if_item1_is_empty(self):
        # setup

        # test
        result = to_cs_string("", "item2")

        # assert
        self.assertEqual(",item2", result)


    def test__return_single_item_if_item2_is_none(self):
        # setup

        # test
        result = to_cs_string("item1", None)

        # assert
        self.assertEqual("item1", result)


    def test__return_single_item_if_item1_is_none(self):
        # setup

        # test
        result = to_cs_string(None, "item2")

        # assert
        self.assertEqual("item2", result)


    def test__return_string_for_both_items(self):
        # setup

        # test
        result = to_cs_string("item1", "item2")

        # assert
        self.assertEqual("item1,item2", result)


    def test__return_multiple_items(self):
        # setup

        # test
        result = to_cs_string("item1,item2,item3,item4")

        # assert
        self.assertEqual("item1,item2,item3,item4", result)


