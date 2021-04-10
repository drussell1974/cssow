from unittest import TestCase
from shared.models.cls_academic_year_period import AcademicYearPeriod

class test_AcademicYearPeriod_validate__name(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)
        
        test.time = "00:01"

        # act
        test.validate()

        # assert
        self.assertFalse("time" in test.validation_errors, "time should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.time = " 00:01 "

        # act
        test.validate()

        # assert
        self.assertFalse("time" in test.validation_errors, "time should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.time, "00:01")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.time = ""

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.time = None

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)
        
        test.time = "23:59"

        # act
        test.validate()

        # assert
        self.assertFalse("time" in test.validation_errors, "time should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.time = "24:00"

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_when_too_short(self):
        # arrange
        test = AcademicYearPeriod("0000", "Lorem ipsum", False)

        test.time = "24:00"

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_when_invalid_sep(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.time = "00#00"

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_when_not_a_number(self):
        # arrange
        test = AcademicYearPeriod("00@00", "Lorem ipsum", False)

        test.time = "0a:00"

        # act
        test.validate()

        # assert
        self.assertTrue("time" in test.validation_errors, "time should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")



class test_institute_validate__name(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)


        test.name = "A"

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.name = " x "

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.name, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.name = ""

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.name = None

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be True")


    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        
        test.name = "Lorem ipsum dolor si" # length 30 characters

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearPeriod("00:00", "Lorem ipsum", False)

        test.name = "Lorem ipsum dolor sit" # length 31 characters

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
