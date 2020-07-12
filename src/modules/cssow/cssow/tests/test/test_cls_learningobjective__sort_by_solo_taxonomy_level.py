from tests.model_test._unittest import TestCase
from web.shared.models.cls_learningobjective import LearningObjectiveModel, sort_by_solo_taxonomy_level


class test__cls_learningobjective__sort_by_solo_taxonomy_level(TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test__return_empty_list(self):
        # setup
        unsorted_list = []

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertEqual([], result)


    def test__return_single_item(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(1, solo_taxonomy_level="a")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 1)


    def test__return_2_items_already_sorted(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(2, solo_taxonomy_level="a"),
            LearningObjectiveModel(1, solo_taxonomy_level="b")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 2)
        self.assertTrue(result[1].id == 1)


    def test__return_2_items_not_sorted(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(1, solo_taxonomy_level="b"),
            LearningObjectiveModel(2, solo_taxonomy_level="a")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 2)
        self.assertTrue(result[1].id == 1)


    def test__return_3_items_already_sorted(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(3, solo_taxonomy_level="a"),
            LearningObjectiveModel(2, solo_taxonomy_level="b"),
            LearningObjectiveModel(1, solo_taxonomy_level="c")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 3)
        self.assertTrue(result[1].id == 2)
        self.assertTrue(result[2].id == 1)


    def test__return_3_items_not_sorted(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(3, solo_taxonomy_level="b"),
            LearningObjectiveModel(1, solo_taxonomy_level="c"),
            LearningObjectiveModel(2, solo_taxonomy_level="a")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 2)
        self.assertTrue(result[1].id == 3)
        self.assertTrue(result[2].id == 1)


    def test__return_3_items_reversed(self):
        # setup
        unsorted_list = [
            LearningObjectiveModel(1, solo_taxonomy_level="c"),
            LearningObjectiveModel(3, solo_taxonomy_level="b"),
            LearningObjectiveModel(2, solo_taxonomy_level="a")
        ]

        # test
        result = sort_by_solo_taxonomy_level(unsorted_list)

        # assert
        self.assertTrue(result[0].id == 2)
        self.assertTrue(result[1].id == 3)
        self.assertTrue(result[2].id == 1)


