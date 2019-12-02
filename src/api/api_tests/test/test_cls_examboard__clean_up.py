from _unittest import TestCase
from cls_examboard import ExamBoardModel


class test_cls_examboard__clean_up(TestCase):

    def setUp(self):
        self.test = ExamBoardModel(1, "")


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
