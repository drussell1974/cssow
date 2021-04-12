from unittest import TestCase, skip
from shared.models.cls_academic_year import AcademicYearModel

class test_AcademicYearModel_validate__start_date(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearModel("1700-01-01T00:00", "2099-12-31T00:00", False)
        
        # act
        #test.start_date = "1700-01-01T00:00"
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")
        

    @skip("checks not implemented")
    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearModel(" 1700-01-01T00:00 ", "2099-12-31T00:00", False)
        
        # act
        #test.start_date = " 1700-01-01T00:00 "
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.start_date, "1700-01-01T00:00")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = AcademicYearModel("1699-12-31T00:00", "2099-12-31T00:00", False)
        
        # act
        #test.start_date = "1699-12-31T00:00"
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")



    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearModel("2099-12-31T00:00", "2099-12-31T00:00", False)
        
        #test.start_date = "2099-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearModel("2100-12-31T00:00", "2100-12-31T00:00", False)

        #test.start_date = "2100-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")

    @skip("checks not implemented")
    def test_max__invalid_when_invalid_sep(self):
        # arrange
        test = AcademicYearModel("2100-12-31T00#00", "2100-12-31T00:00", False)

        #test.start_date = "2100-12-31T00#00"

        # act
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")

    @skip("checks not implemented")
    def test_max__invalid_when_not_a_number(self):
        # arrange
        test = AcademicYearModel("2100-12-31T0a:00", "2100-12-31T00:00", False)

        #test.start_date = "2100-12-31T0a:00"

        # act
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


class test_AcademicYearModel_validate__end_date(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearModel("1700-01-01T00:00", "1700-01-01T00:00", False)
        
        # act
        #test.end_date = "1700-01-01T00:00"
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")
        

    @skip("checks not implemented")
    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearModel(" 1700-01-01T00:00 ", "2099-12-31T00:00", False)
        
        # act
        #test.end_date = " 1700-01-01T00:00 "
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.end_date, "1700-01-01T00:00")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = AcademicYearModel("2099-12-31T00:00", "1699-12-31T00:00", False)
        
        # act
        #test.end_date = "1699-12-31T00:00"
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")



    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearModel("2099-12-31T00:00", "2099-12-31T00:00", False)
        
        #test.end_date = "2099-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearModel("2100-12-31T00:00", "2100-12-31T00:00", False)

        #test.end_date = "2100-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")

    @skip("checks not implemented")
    def test_max__invalid_when_invalid_sep(self):
        # arrange
        test = AcademicYearModel("2100-12-31T00#00", "2100-12-31T00:00", False)

        #test.end_date = "2100-12-31T00#00"

        # act
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")

    @skip("checks not implemented")
    def test_max__invalid_when_not_a_number(self):
        # arrange
        test = AcademicYearModel("2100-12-31T0a:00", "2100-12-31T00:00", False)

        #test.end_date = "2100-12-31T0a:00"

        # act
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")

