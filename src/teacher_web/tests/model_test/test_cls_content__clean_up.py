from unittest import TestCase
from shared.models.cls_content import ContentModel

class test_cls_content__clean_up(TestCase):

    def setUp(self):
        self.test = ContentModel(1, "", "")

    # description

    def test_description__trim_whitespace(self):

        self.test.description = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.description)


    # letter_prefix

    def test_letter_prefix__trim_whitespace(self):

        self.test.letter_prefix = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.letter_prefix)
