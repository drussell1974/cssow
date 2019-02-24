import sys
sys.path.append('../../schemeofwork/modules')
from cls_solotaxonomy import SoloTaxonomyModel

from unittest import TestCase

class test_cls_solotaxonomy__clean_up(TestCase):

    def setUp(self):
        self.test = SoloTaxonomyModel(1, "", "")


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)


    def test_lvl__trim_whitespace(self):

        self.test.lvl = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.lvl)
