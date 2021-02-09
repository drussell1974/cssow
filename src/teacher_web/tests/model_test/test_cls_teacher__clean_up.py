from unittest import TestCase
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel


from unittest import TestCase

class test_cls_department__clean_up(TestCase):

    def setUp(self):
        self.test = TeacherModel(1, name="", department=DepartmentModel(0, ""))


    # title

    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

