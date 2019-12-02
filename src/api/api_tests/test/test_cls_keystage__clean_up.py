import sys
sys.path.append('../../schemeofwork/modules')
from cls_keystage import KeyStageModel

from unittest import TestCase

class test_cls_keystage__clean_up(TestCase):

    def setUp(self):
        self.test = KeyStageModel(1, "")


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)


    def test_name__escape_sqlterminator(self):

        self.test.name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.name)


    def test_name__escape_quote(self):

        self.test.name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.name)
