import sys
sys.path.insert(0, '../../schemeofwork/modules/')

from schemeofwork_testcase import SchemeOfWork_TestCase


class test_SchemeOfWork_clean_up__key_stage_name(SchemeOfWork_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")

class test_SchemeOfWork_clean_up__exam_board_name(SchemeOfWork_TestCase):

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")
