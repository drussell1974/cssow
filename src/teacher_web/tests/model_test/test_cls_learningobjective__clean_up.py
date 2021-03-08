from unittest import TestCase
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


class test_learningobjective__clean_up__notes(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.notes = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.notes, "x")


class test_learningobjective__clean_up__missing_words_challenge(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.missing_words_challenge = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.missing_words_challenge, "x")


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
