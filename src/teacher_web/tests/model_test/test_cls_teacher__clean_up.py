from unittest import TestCase, skip
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel


from unittest import TestCase

@skip("Depreciate TeacherModel and use TeacherPermissionModel")
class test_cls_teacher__clean_up(TestCase):

    def setUp(self):
        self.test = TeacherModel(1, "", department=DepartmentModel(0, "", institute = InstituteModel(0, name="")))
        

    # title

    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

