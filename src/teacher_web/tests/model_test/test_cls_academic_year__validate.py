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
        test = AcademicYearModel(1700, "1700-01-01", "2099-12-31", False)
        
        # act
        #test.start_date = "1700-01-01T00:00"
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")
        

    @skip("checks not implemented")
    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearModel(1700, " 1700-01-01T00:00 ", "2099-12-31T00:00", False)
        
        # act
        #test.start_date = " 1700-01-01T00:00 "
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.start_date, "1700-01-01T00:00")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange NOTE: year/id is valid
        test = AcademicYearModel(1700, "1699-12-31", "2099-12-31", False)
        
        # act
        #test.start_date = "1699-12-31T00:00"
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")



    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearModel(2099, "2099-12-31", "2099-12-31", False)
        
        #test.start_date = "2099-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertFalse("start_date" in test.validation_errors, "start_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearModel(1700, "2100-12-31", "2100-12-31", False)

        #test.start_date = "2100-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertTrue("start_date" in test.validation_errors, "start_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_when_invalid_sep(self):
        # act
        with self.assertRaises(ValueError): 
            AcademicYearModel(2100, "2100-12-31T00#00", "2100-12-31T00:00", False)


    def test_max__invalid_when_not_a_number(self):
        # arrange
        with self.assertRaises(ValueError):
            AcademicYearModel(2100, "2100-12-31T0a:00", "2100-12-31T00:00", False)


class test_AcademicYearModel_validate__end_date(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearModel(1700, "1700-01-01", "1700-01-01", False)
        
        # act
        #test.end_date = "1700-01-01T00:00"
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")
        

    @skip("checks not implemented")
    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearModel(1700, " 1700-01-01T00:00 ", "2099-12-31T00:00", False)
        
        # act
        #test.end_date = " 1700-01-01T00:00 "
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.end_date, "1700-01-01T00:00")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = AcademicYearModel(2099, "2099-12-31", "1699-12-31", False)
        
        # act
        #test.end_date = "1699-12-31T00:00"
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")



    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearModel(2099, "2099-12-31", "2099-12-31", False)
        
        #test.end_date = "2099-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertFalse("end_date" in test.validation_errors, "end_date should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearModel(2100, "2100-12-31", "2100-12-31", False)

        #test.end_date = "2100-12-31T00:00"

        # act
        test.validate()

        # assert
        self.assertTrue("end_date" in test.validation_errors, "end_date should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__invalid_when_invalid_sep(self):
        # assert

        with self.assertRaises(ValueError): 
            AcademicYearModel(2100, "2100-12-31T00:00", "2100-12-31T00:00", False)


    def test_max__invalid_when_not_a_number(self):
        # assert

        with self.assertRaises(ValueError): 
            AcademicYearModel(2100, "2100-12-AA", "2100-12-31", False)



class test_AcademicYearModel_validate__year(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass

    
    def test_min__valid_extreme(self):
        # arrange
        test = AcademicYearModel(1700, "1700-01-01", "2099-12-31", False)
        
        # act
        
        test.validate()

        # assert NOTE: id is year
        self.assertFalse("id" in test.validation_errors, "year should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")
        

    @skip("checks not implemented")
    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = AcademicYearModel(1700, "1700-01-01", "2099-12-31", False)

        # act
        
        test.validate()

        # assert NOTE: id is year
        self.assertFalse("id" in test.validation_errors, "year should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.id, "1700-01-01T00:00")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = AcademicYearModel(1699, "1700-01-01", "2099-12-31", False)

        # act
        test.validate()

        # assert NOTE: id is year
        self.assertTrue("id" in test.validation_errors, "year should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")



    def test_max__valid_extreme(self):
        # arrange
        test = AcademicYearModel(1700, "1700-01-01", "2099-12-31", False)

        # act
        test.validate()

        # assert NOTE: id is year
        self.assertFalse("id" in test.validation_errors, "year should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = AcademicYearModel(2100, "1700-01-01", "2099-12-31", False)

        # act
        test.validate()

        # assert NOTE: id is year
        self.assertTrue("id" in test.validation_errors, "year should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
