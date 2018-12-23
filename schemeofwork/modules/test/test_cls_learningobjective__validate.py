
from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_learningobjective import LearningObjectiveModel
from learningobjective_testcase import LearningObjective_TestCase

"""

description DONE
solo_taxonomy_id DOING
solo_taxonomy_name = ""
solo_taxonomy_level = ""
topic_id = 0
topic_name = ""
parent_topic_id = 0
parent_topic_name = ""
content_id = 0
content_description = ""
exam_board_id = 0
exam_board_name = ""
learning_episode_id = 0
learning_episode_name = ""
key_stage_id = 0
key_stage_name = ""
parent_id = None

"""
class test_LearningObjectiveModel_validate__description(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.description = "A"

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.description = " x "

        # test
        test.validate()

        # assert
        self.assertEqual(test.description, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should have no validation errors - %s" % test.validation_errors)

    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.description = ""

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.description = None

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit ame" # length 25 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("description" in test.validation_errors, "description should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.description = "Lorem ipsum dolor sit amet" # length 25 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("description" in test.validation_errors, "description should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningObjectiveModel_validate__exam_board_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.exam_board_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.exam_board_id = 0 # values should not be negative

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "should not be is_valid")
        self.assertTrue("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.exam_board_id = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.exam_board_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("exam_board_id" in test.validation_errors, "exam_board_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.exam_board_id = 10000 # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("exam_board_id" in test.validation_errors, "exam_board_id should have validation error %s" % test.validation_errors)

"""
class est_SchemeOfWork_clean_up__exam_board_name(LearningObjective_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")


class est_SchemeOfWork_validate__key_stage_id(LearningObjective_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.key_stage_id = 1

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.key_stage_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.key_stage_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.key_stage_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_stage_id" in test.validation_errors, "key_stage_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.key_stage_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("key_stage_id" in test.validation_errors, "key_stage_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
"""

