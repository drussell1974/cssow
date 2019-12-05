from _unittest import TestCase
from cls_solotaxonomy import SoloTaxonomyModel


class test_cls_solotaxonomy__clean_up(TestCase):

    def setUp(self):
        self.test = SoloTaxonomyModel(1, "", "")


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


    def test_lvl__trim_whitespace(self):

        self.test.lvl = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.lvl)


    def test_lvl__escape_sqlterminator(self):

        self.test.lvl = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.lvl)


    def test_lvl__escape_quote(self):

        self.test.lvl = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.lvl)
