from tests.model_test._unittest import TestCase
from tests.model_test.learningobjective_testcase import LearningObjective_TestCase


class test_learningobjective__clean_up__parent_topic_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.parent_topic_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.parent_topic_name, "x")


    def test__escape_sqlterminator(self):

        self.test.parent_topic_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.parent_topic_name)


    def test__escape_quote(self):

        self.test.parent_topic_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.parent_topic_name)


class test_learningobjective__clean_up__content_description(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.content_description = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.content_description, "x")


    def test__escape_sqlterminator(self):

        self.test.content_description = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.content_description)


    def test__escape_quote(self):

        self.test.content_description = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.content_description)


class test_learningobjective__clean_up__lesson_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.lesson_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.lesson_name, "x")


    def test__escape_sqlterminator(self):

        self.test.lesson_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.lesson_name)


    def test__escape_quote(self):

        self.test.lesson_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.lesson_name)


class test_learningobjective__clean_up__key_stage_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")


    def test__escape_sqlterminator(self):

        self.test.key_stage_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_stage_name)


    def test__escape_quote(self):

        self.test.key_stage_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_stage_name)


class test_learningobjective__clean_up__key_words(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_words = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual("x", test.key_words)


    def test__multiple_items(self):
        test = self._construct_valid_object()

        test.key_words = "w x, y, z "

        # test
        test._clean_up()

        # assert
        self.assertEqual("w x,y,z", test.key_words)


    def test__escape_sqlterminator(self):

        self.test.key_words = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_words)


    def test__escape_quote(self):

        self.test.key_words = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_words)
