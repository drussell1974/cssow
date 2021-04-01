from unittest import TestCase
from shared.models.cls_ks123pathway import KS123PathwayModel


class test_cls_ks123pathway__clean_up(TestCase):

    def setUp(self):
        self.test = KS123PathwayModel(1, "", ctx=None)


    def test_objective__trim_whitespace(self):

        self.test.objective = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.objective)

