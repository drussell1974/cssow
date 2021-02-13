from unittest import TestCase, skip
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel

@skip("Depreciate TeacherModel and use TeacherPermissionModel")
class test_cls_teacher__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = TeacherModel(0, "Dave Russell", department=DepartmentModel(67, "Testing Department", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Dave Russell", self.test.name)
        self.assertEqual("Testing Department", self.test.department.name)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # setup

        self.test = TeacherModel(6079, "Sor shurem", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        # self.test
        self.test.validate()

        # assert
        self.assertEqual(6079, self.test.id)
        self.assertEqual("Sor shurem", self.test.name)
        self.assertEqual("Computer Science", self.test.department.name)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
