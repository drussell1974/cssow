from unittest import TestCase
from tests.model_test.learningepisode_testcase import Lesson_TestCase

class test_LessonModel__clean_up___scheme_of_work_name(Lesson_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()


    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.scheme_of_work_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.scheme_of_work_name, "x")


class test_LessonModel_clean_up__key_stage_name(Lesson_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")


class test_LessonModel_clean_up__pathway_objective_ids(Lesson_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = [" x "]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x"], test.pathway_objective_ids)


    def test__multiple_items(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = [" x", " y", "z "]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x","y","z"], test.pathway_objective_ids)


    def test__remove_duplicates(self):
        test = self._construct_valid_object()

        test.pathway_objective_ids = ["x", "y", "z", "y"]

        # test
        test._clean_up()

        # assert
        self.assertEqual(["x", "y", "z"], test.pathway_objective_ids)

