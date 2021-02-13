from unittest import TestCase
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel


class test_cls_department__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee

        self.test = DepartmentModel(0, "Lorem ipsum", institute=InstituteModel(2, "Lorem Ipsum"))

        # assert
        self.assertEqual(0, self.test.id)
        self.assertEqual("Lorem ipsum", self.test.name)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # arrange

        self.test = DepartmentModel(1, "Sor shurem", institute=InstituteModel(2, "Lorem Ipsum"))

        # self.test
        self.test.validate()

        # assert
        self.assertEqual(1, self.test.id)
        self.assertEqual("Sor shurem", self.test.name)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
