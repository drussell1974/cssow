from unittest import TestCase
from shared.models.core.helper_string import merge_string_list

class test__helper_string__merge_stringlist(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test__return_empty_string_if_both_strings_are_empty(self):
        # setup

        # test
        result = merge_string_list("", "", ",")

        # assert
        self.assertEqual([], result)


    def test__return_single_item_from_list1_if_list2_is_empty(self):
        # setup

        # test
        result = merge_string_list("item1 from list1", "", ",")

        # assert
        self.assertEqual(["item1 from list1"], result)


    def test__return_single_item_from_list2_if_list1_is_empty(self):
        # setup

        # test
        result = merge_string_list("", "item1 from list2", ",")

        # assert
        self.assertEqual(["item1 from list2"], result)


    def test__return_single_items_from_both_lists(self):
        # setup

        # test
        result = merge_string_list("item1 from list1", "item1 from list2", ",")

        # assert
        self.assertEqual(["item1 from list1","item1 from list2"], result)


    def test__return_single_item_from_both_lists_where_both_lists_are_the_same(self):
        # setup

        # test
        result = merge_string_list("item", "item", ",")

        # assert
        self.assertEqual(["item"], result)


    def test__return_multiple_items_from_list1_where_list2_is_empty(self):
        # setup

        # test
        result = merge_string_list("item1 from list1,item2 from list1", "", ",")

        # assert
        self.assertEqual(["item1 from list1","item2 from list1"], result)


    def test__return_multiple_items_from_list2_where_list1_is_empty(self):
        # setup

        # test
        result = merge_string_list("", "item1 from list2,item2 from list2", ",")

        # assert
        self.assertEqual(["item1 from list2","item2 from list2"], result)


    def test__return_multiple_items_from_both_lists_where_items_are_unique(self):
        # setup

        # test
        result = merge_string_list("item1 from list1,item2 from list1", "item1 from list2,item2 from list2", ",")

        # assert
        self.assertEqual(["item1 from list1","item1 from list2","item2 from list1","item2 from list2"], result)


    def test__return_multiple_items_from_both_lists_where_lists_are_duplicate(self):
        # setup

        # test
        result = merge_string_list("item1,item2", "item1,item2", ",")

        # assert
        self.assertEqual(["item1","item2"], result)


    def test__return_should_handle_reversed_items(self):
        # setup

        # test
        result = merge_string_list("item2,item1", "item1,item2", ",")

        # assert
        self.assertEqual(["item1","item2"], result)


    def test__return_multiple_items_from_both_lists_where_one_item_in_list_is_a_duplicate_and_1_unique(self):
        # setup

        # test
        result = merge_string_list("item1,item2", "item1,item3", ",")

        # assert
        self.assertEqual(["item1","item2","item3"], result)


    def test__return_multiple_items_from_both_lists_where_one_item_in_the_list_is_a_duplicate(self):
        # setup

        # test
        result = merge_string_list("item3,item2,item3", "item1,item2,item4", ",")

        # assert
        self.assertEqual(["item1","item2","item3","item4"], result)


