from unittest import TestCase
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

class test_cls_teacher__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # self.test
        self.test = TeacherModel(0, name="Lorem ipsum", department=DepartmentModel(1, "Testing Department"))

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Lorem ipsum", self.test.name)
        self.assertEqual("Testing Department", self.test.department.name)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # setup

        self.test = TeacherModel(1, name="Sor shurem", department=DepartmentModel(34, "Testing Department"))

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Sor shurem", self.test.name)
        self.assertEqual("Testing Department", self.test.department.name)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
