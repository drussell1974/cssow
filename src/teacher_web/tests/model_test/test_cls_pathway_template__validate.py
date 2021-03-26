from unittest import TestCase, skip
from shared.models.cls_pathway_template import PathwayTemplateModel as Model


class test_cls_pathway__validate__department_id(TestCase):

    test = None

    def setUp(self):
        # start with valid model exept attribute under test
        self.test = Model(1, name="Lorem")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.department_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("department_id" in self.test.validation_errors, "department_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.department_id = 0

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_id" in self.test.validation_errors, "department_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.department_id = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("department_id" in self.test.validation_errors, "department_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.department_id = Model.MAX_INT

        # test
        self.test.validate()

        # assert
        self.assertFalse("department_id" in self.test.validation_errors, "department_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.department_id = Model.MAX_INT + 1
        # test
        self.test.validate()

        # assert
        self.assertTrue("department_id" in self.test.validation_errors, "department_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
