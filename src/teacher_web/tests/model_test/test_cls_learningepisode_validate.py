from unittest import TestCase
from tests.model_test.learningepisode_testcase import Lesson_TestCase


class test_LessonModel_validate__title(Lesson_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__invalid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.title = ""

        # test
        test.validate()

        # assert
        self.assertEqual(test.title, "")
        self.assertFalse(test.is_valid, "is_valid should be True")
        self.assertTrue("title" in test.validation_errors, "title should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.title = "  "

        # test
        test.validate()

        # assert
        self.assertEqual(test.title, "")
        self.assertFalse(test.is_valid, "is_valid should be True")
        self.assertTrue("title" in test.validation_errors, "title should have no validation errors - %s" % test.validation_errors)


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.title = "Data Representation: Sound"

        # test
        test.validate()

        # assert
        self.assertEqual(test.title, "Data Representation: Sound")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("summary" in test.validation_errors, "summary should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        test = self._construct_valid_object()

        test.title = " Data Representation: Sound "

        # test
        test.validate()

        # assert
        self.assertEqual(test.title, "Data Representation: Sound")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("title" in test.validation_errors, "title should have no validation errors - %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):

        test = self._construct_valid_object()

        test.title = None

        # test
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("title" in test.validation_errors, "title should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):

        test = self._construct_valid_object()

        test.title = "Lorem ipsum dolor sit amet, consectetur adipi" # 45 characters

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")

        self.assertFalse("title" in test.validation_errors, "title should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):

        test = self._construct_valid_object()

        test.title = "Lorem ipsum dolor sit amet, consectetur adipis" # 46 characters + 1

        # test
        test.validate()

        # assert
        self.assertTrue("title" in test.validation_errors, "title should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_LessonModel__validate__order_of_delivery_id(Lesson_TestCase):

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


class test_LessonModel__validate__topic_id(Lesson_TestCase):

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


class test_LessonModel__validate__scheme_of_work_id(Lesson_TestCase):

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


class test_LessonModel__validate__key_stage_id(Lesson_TestCase):

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


class test_LessonModel_validate__summary(Lesson_TestCase):

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


class test_LessonModel__validate__year_id(Lesson_TestCase):

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
