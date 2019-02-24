import sys
sys.path.append('../../schemeofwork/modules')
from cls_examboard import ExamBoardModel

from unittest import TestCase

class test_cls_examboard__clean_up(TestCase):

    def setUp(self):
        self.test = ExamBoardModel(1, "")


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)
