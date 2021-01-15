from unittest import TestCase
from tests.model_test.learningobjective_testcase import LearningObjective_TestCase
from shared.models.cls_department import DepartmentModel

class test_Department_validate__name(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")

        test.name = "A"

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")

        test.name = " x "

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.name, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")

    def test_min__invalid_extreme(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")

        test.name = ""

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")

        test.name = None

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")
        
        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse e" # length 70 characters

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = DepartmentModel(1, "Lorem ipsum")

        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse el"  # length 71 characters

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
