from tests.model_test._unittest import TestCase
from shared.models.cls_keystage import KeyStageModel


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
