import sys
sys.path.append('../../schemeofwork/modules/')

from schemeofwork_testcase import SchemeOfWork_TestCase


class test_SchemeOfWork__get_ui_sub_heading(SchemeOfWork_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with_keystage_and_examboard(self):
        # set up
        test = self._construct_valid_object()

        test.key_stage_name = "KS3"
        test.exam_board_name = "OCR"

        # test
        val = test.get_ui_sub_heading()

        # assert
        self.assertEqual("KS3 - OCR", val)


    def test_with_keystage_only(self):
        # set up
        test = self._construct_valid_object()

        test.exam_board_name = None
        test.key_stage_name = "KS1"

        # test
        val = test.get_ui_sub_heading()

        # assert
        self.assertEqual("KS1", val)


class test_SchemeOfWork__get_ui_title(SchemeOfWork_TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_with_name(self):
        # set up
        test = self._construct_valid_object()

        # test
        val = test.get_ui_title()

        # assert
        self.assertEqual("test name", val)
