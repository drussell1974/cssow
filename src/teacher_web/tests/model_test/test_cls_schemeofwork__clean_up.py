from unittest import TestCase
from tests.model_test.schemeofwork_testcase import SchemeOfWork_TestCase


class test_SchemeOfWork_clean_up__key_stage_name(SchemeOfWork_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):

        self.test.key_stage_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(self.test.key_stage_name, "x")



class test_SchemeOfWork_clean_up__exam_board_name(SchemeOfWork_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):

        self.test.exam_board_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(self.test.exam_board_name, "x")


class test_SchemeOfWork_clean_up__department_name(SchemeOfWork_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):

        self.test.department_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(self.test.department_name, "x")


class test_SchemeOfWork_clean_up__school_name(SchemeOfWork_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):

        self.test.school_name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual(self.test.school_name, "x")
