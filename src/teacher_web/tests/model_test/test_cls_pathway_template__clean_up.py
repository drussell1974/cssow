from unittest import TestCase
from shared.models.cls_pathway_template import PathwayTemplateModel


class test_cls_pathway_template__clean_up(TestCase):

    def setUp(self):
        self.test = PathwayTemplateModel(1, "", 0)


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

