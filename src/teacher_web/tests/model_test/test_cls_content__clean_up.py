from tests.model_test._unittest import TestCase
from shared.models.cls_content import ContentModel

class test_cls_content__clean_up(TestCase):

    def setUp(self):
        self.test = ContentModel(1, "")


    def test_description__trim_whitespace(self):

        self.test.description = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.description)


    def test_description__escape_sqlterminator(self):

        self.test.description = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.description)


    def test_description__escape_quote(self):

        self.test.description = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.description)
