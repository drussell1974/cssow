from unittest import TestCase, skip
from unittest.mock import patch
from shared.models.cls_lesson_schedule import LessonScheduleModel as Model
from tests.test_helpers.mocks import fake_ctx_model, fake_lesson_schedule


class test_cls_lesson_schedule__validate__class_code(TestCase):

    test = None

    def setUp(self):
        # start with valid model exept attribute under test
        
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = fake_lesson_schedule(1, title="Vivamus at porta orci", start_date=None, class_name="7x", class_code = "", lesson_id=9734, scheme_of_work_id=3434, auth_ctx=mock_auth_user)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.class_code = "ABCDEF"

        # test
        self.test.validate()

        # assert
        self.assertFalse("class_code" in self.test.validation_errors, "class_code should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme_trim_whitespace(self):
        # set up

        self.test.class_code = " "

        # test
        self.test.validate()

        # assert
        self.assertTrue("class_code" in self.test.validation_errors, "class_code should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.class_code, "")
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange

        self.test.class_code = ""

        # act
        self.test.validate()

        # assert
        self.assertTrue("class_code" in self.test.validation_errors, "class_code should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # assert

        self.test.class_code = None

        # act
        self.test.validate()

        # assert
        self.assertTrue("class_code" in self.test.validation_errors, "class_code should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        
        self.test.class_code = "ABCDEF"

        # act
        self.test.validate()

        # assert
        self.assertFalse("class_code" in self.test.validation_errors, "class_code should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange

        self.test.class_code = "ABCDEFG" 
        
        # act
        self.test.validate()

        # assert
        self.assertTrue("class_code" in self.test.validation_errors, "class_code should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_lesson_schedule__validate__class_name(TestCase):

    test = None

    def setUp(self):
        # start with valid model exept attribute under test
        
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:    
            self.test = fake_lesson_schedule(1, title="Vivamus at porta orci", start_date=None, class_name="", class_code = "ABCDEF", lesson_id=9734, scheme_of_work_id=3434, auth_ctx=mock_auth_user)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.class_name = "ABCDEFGHIJ"

        # test
        self.test.validate()

        # assert
        self.assertFalse("class_name" in self.test.validation_errors, "class_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme_trim_whitespace(self):
        # set up

        self.test.class_name = " "

        # test
        self.test.validate()

        # assert
        self.assertTrue("class_name" in self.test.validation_errors, "class_name should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.class_name, "")
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange

        self.test.class_name = ""

        # act
        self.test.validate()

        # assert
        self.assertTrue("class_name" in self.test.validation_errors, "class_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # assert

        self.test.class_name = None

        # act
        self.test.validate()

        # assert
        self.assertTrue("class_name" in self.test.validation_errors, "class_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        
        self.test.class_name = "ABCDEFGHIJ"

        # act
        self.test.validate()

        # assert
        self.assertFalse("class_name" in self.test.validation_errors, "class_name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange

        self.test.class_name = "ABCDEFGHIJK" 
        
        # act
        self.test.validate()

        # assert
        self.assertTrue("class_name" in self.test.validation_errors, "class_name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")

