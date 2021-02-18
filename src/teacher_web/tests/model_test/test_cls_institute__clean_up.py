from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel

from unittest import TestCase

@skip("not implemented")
class test_cls_institute__clean_up(TestCase):

    def setUp(self):
        self.test = InstituteModel(1, name="")


    # title

    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)


    def test_description__trim_whitespace(self):

        self.test.description = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.description)
