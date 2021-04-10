from unittest import TestCase
from shared.models.cls_academic_year_period import AcademicYearPeriod

class test_cls_academic_year_period__constructor(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_constructor_default(self):

        # arrangee

        self.test = AcademicYearPeriod("", "", is_from_db=False)

        # assert
        self.assertEqual("", self.test.time)
        self.assertEqual("", self.test.name)
        self.assertFalse(self.test.is_valid)
        self.assertTrue(self.test.is_new())


    def test_constructor_set_valid_values(self):

        # arrange

        self.test = AcademicYearPeriod("10:00", "10am (Period 1)", is_from_db=True)

        # self.test
        self.test.validate()

        # assert
        self.assertEqual("10:00", self.test.time)
        self.assertEqual("10am (Period 1)", self.test.name)
        self.assertEqual({}, self.test.validation_errors)
        self.assertTrue(self.test.is_valid)
        self.assertFalse(self.test.is_new())
