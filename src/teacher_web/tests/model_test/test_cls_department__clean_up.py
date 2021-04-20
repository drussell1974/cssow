from unittest import TestCase
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel

class test_cls_department__clean_up(TestCase):

    def setUp(self):
        self.test = DepartmentModel(1, "", topic_id=3, hod_id=56, institute=InstituteModel(2, ""))

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