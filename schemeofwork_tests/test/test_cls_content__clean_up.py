import sys
sys.path.append('../../schemeofwork/modules')
from cls_content import ContentModel

from unittest import TestCase

class test_cls_content__clean_up(TestCase):

    def setUp(self):
        self.test = ContentModel(1, "")


    def test_description__trim_whitespace(self):

        self.test.description = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.description)


    def test_description__remove_sqlterminator(self):

        self.test.description = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.description)