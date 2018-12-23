
from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_learningepisode import LearningEpisodeModel

class Test_LearningEpisode_Constructor(TestCase):

    test = None

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_validate_for_default_instance_returns_false(self):

        # setup
        test = LearningEpisodeModel(0)

        # test
        test.validate()

        # validate
        self.assertFalse(test.is_valid)


    def test_constructor_default(self):

        # test
        test = LearningEpisodeModel(0)

        # assert
        self.assertEqual(0, test.id)
        self.assertEqual(1, test.order_of_delivery_id, "order_of_delivery_id should be 0")
        self.assertEqual(0, test.scheme_of_work_id, "scheme_of_work_id should be 0")
        self.assertEqual("", test.scheme_of_work_name, "scheme_of_work_name should be ''")
        self.assertEqual(0, test.topic_id, "topic_id should be 0")
        self.assertEqual("", test.topic_name, "topic_name should be ''")
        self.assertEqual(0, test.parent_topic_id, "parent_topic_id should be 0")
        self.assertEqual("", test.parent_topic_name)
        self.assertEqual(0, test.key_stage_id, "key_stage_id should be 0")
        self.assertEqual("", test.key_stage_name, "key_stage_name should be ''")
        self.assertEqual(False, test.is_valid, "is_valid should be False")
        self.assertTrue(len(test.validation_errors) == 0)


    def test_constructor_set_valid_values(self):

        # setup

        test = LearningEpisodeModel(1,
                                 order_of_delivery_id=2,
                                 scheme_of_work_id=3,
                                 topic_id=4,
                                 parent_topic_id=5,
                                 key_stage_id=6)

        # test
        test.validate()

        # assert
        self.assertEqual(1, test.id)
        self.assertEqual(2, test.order_of_delivery_id)
        self.assertEqual(3, test.scheme_of_work_id)
        self.assertEqual(4, test.topic_id)
        self.assertEqual(5, test.parent_topic_id)
        self.assertEqual(6, test.key_stage_id)
        self.assertTrue(test.is_valid)
