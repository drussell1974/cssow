
from unittest import TestCase

import sys
sys.path.insert(0, '../')

from cls_learningepisode import LearningEpisodeModel

class TestCase_LearningEpisodeModel_Base(TestCase):
    """ Shared functions """
    def _construct_valid_object(self):#
        """ Create a valid Object """
        # set up
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

        return test


class TestCase_LearningEpisodeModel__order_of_delivery_id(TestCase_LearningEpisodeModel_Base):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.order_of_delivery_id = 1
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("order_of_delivery_id" in test.validation_errors, "order_of_delivery_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.order_of_delivery_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("order_of_delivery_id" in test.validation_errors, "order_of_delivery_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.order_of_delivery_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("order_of_delivery_id" in test.validation_errors, "order_of_delivery_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()
        test.order_of_delivery_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("order_of_delivery_id" in test.validation_errors, "order_of_delivery_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.order_of_delivery_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("order_of_delivery_id" in test.validation_errors, "order_of_delivery_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class TestCase_LearningEpisodeModel__topic_id(TestCase_LearningEpisodeModel_Base):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.topic_id = 1
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("topic_id" in test.validation_errors, "topic_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.topic_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("topic_id" in test.validation_errors, "topic_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.topic_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("topic_id" in test.validation_errors, "topic_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()
        test.topic_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("topic_id" in test.validation_errors, "topic_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.scheme_of_work_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class TestCase_LearningEpisodeModel__scheme_of_work_id(TestCase_LearningEpisodeModel_Base):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.scheme_of_work_id = 1
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.scheme_of_work_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.scheme_of_work_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()
        test.scheme_of_work_id = 9999

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.scheme_of_work_id = 10000  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in test.validation_errors, "scheme_of_work_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class TestCase_LearningEpisodeModel__key_stage_id(TestCase_LearningEpisodeModel_Base):

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
