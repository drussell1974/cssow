import sys
sys.path.append('../../schemeofwork/modules')
from cls_ks123pathway import KS123PathwayModel

from unittest import TestCase

class test_cls_ks123pathway__clean_up(TestCase):

    def setUp(self):
        self.test = KS123PathwayModel(1, "")


    def test_objective__trim_whitespace(self):

        self.test.objective = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.objective)


    def test_term__escape_sqlterminator(self):

        self.test.objective = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.objective)


    def test_term__escape_quote(self):

        self.test.objective = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.objective)
