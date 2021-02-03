from unittest import TestCase
from shared.models.cls_department import DepartmentModel

from unittest import TestCase

class test_cls_department__clean_up(TestCase):

    def setUp(self):
        self.test = DepartmentModel(1, name="")


    # title

    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

