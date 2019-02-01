import sys
sys.path.append('../../schemeofwork/modules')

from learningepisode_testcase import LearningEpisode_TestCase


class test_LearningEpisodeModel__validate__order_of_delivery_id(LearningEpisode_TestCase):

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


class test_LearningEpisodeModel__validate__topic_id(LearningEpisode_TestCase):

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


class test_LearningEpisodeModel__validate__scheme_of_work_id(LearningEpisode_TestCase):

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


class test_LearningEpisodeModel__validate__key_stage_id(LearningEpisode_TestCase):

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


class test_LearningEpisodeModel_validate__key_words(LearningEpisode_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.key_words = ""

        # test
        test.validate()

        # assert
        self.assertEqual(test.key_words, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_words" in test.validation_errors, "key_words should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_words = "  "

        # test
        test.validate()

        # assert
        self.assertEqual(test.key_words, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_words" in test.validation_errors, "key_words should have no validation errors - %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.key_words = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be False")
        self.assertFalse("key_words" in test.validation_errors, "key_words should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.key_words = "Lorem, ipsum, dolor, sit,amet, consectetur, adipiscing, ut elit, Mauris, elementum torro, suscipit, faucibus, Quisque, malesuada, lorem" # l5 keywords

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("key_words" in test.validation_errors, "key_words should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.key_words = "Lorem, ipsum, dolor, sit, amet, consectetur, adipiscing, elit, Nulla, ut nunc, quis, est ornare, tincidunt, Vivamus, aliquet elementum, ipsum vel." # 15 keywords + 1

        # test
        test.validate()

        # assert
        self.assertTrue("key_words" in test.validation_errors, "key_words should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningEpisodeModel_validate__summary(LearningEpisode_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.summary = ""

        # test
        test.validate()

        # assert
        self.assertEqual(test.summary, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("summary" in test.validation_errors, "summary should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.summary = "  "

        # test
        test.validate()

        # assert
        self.assertEqual(test.summary, "")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("summary" in test.validation_errors, "summary should have no validation errors - %s" % test.validation_errors)


    def test_min__valid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.summary = None

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be False")
        self.assertFalse("summary" in test.validation_errors, "summary should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat." # 80 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")

        self.assertFalse("summary" in test.validation_errors, "summary should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpeat." # 80 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("summary" in test.validation_errors, "summary should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LearningEpisodeModel__validate__year_id(LearningEpisode_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.year_id = 1
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("year_id" in test.validation_errors, "year_id should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.year_id = 0

        # test
        test.validate()

        # assert
        self.assertTrue("year_id" in test.validation_errors, "year_id should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.year_id = None

        # test
        test.validate()

        # assert
        self.assertTrue("year_id" in test.validation_errors, "year_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()
        test.year_id = 13

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("year_id" in test.validation_errors, "year_id should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.year_id = 14  # too far out of possible range

        # test
        test.validate()

        # assert
        self.assertTrue("year_id" in test.validation_errors, "year_id should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
