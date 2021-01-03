from unittest import TestCase, skip
from tests.model_test.learningepisode_testcase import Lesson_TestCase
from shared.models.cls_registereduser import RegisteredUserModel


@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -this model cls_registereduser.RegisterUserModel may not be required")
class test_RegsteredUserModel_validate__first_name(Lesson_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__invalid_extreme(self):
        # set up
        test = RegisteredUserModel()

        # test
        test.validate()

        # assert
        self.assertEqual(test.first_name, "")
        self.assertFalse(test.is_valid, "is_valid should be True")
        self.assertTrue("first_name" in test.validation_errors, "first_name should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme_trim_whitespace(self):
        # arrange
        test = RegisteredUserModel()

        test.first_name = "  "

        # act
        test.validate()

        # assert
        self.assertEqual(test.first_name, "")
        self.assertFalse(test.is_valid, "is_valid should be True")
        self.assertTrue("first_name" in test.validation_errors, "first_name should have no validation errors - %s" % test.validation_errors)


    def test_min__valid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        test.first_name = "Data Representation: Sound"

        # act
        test.validate()

        # assert
        self.assertEqual(test.first_name, "Data Representation: Sound")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("first_name" in test.validation_errors, "first_name should not have validation error %s" % test.validation_errors)


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = RegisteredUserModel()

        test.first_name = " Lorem "

        # act
        test.validate()

        # assert
        self.assertEqual(test.first_name, "Lorem")
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("first_name" in test.validation_errors, "first_name should have no validation errors - %s" % test.validation_errors)


    def test_min__invalid_extreme_when_None(self):
        # set up
        test = RegisteredUserModel()

        test.first_name = None

        # act
        test.validate()

        # assert
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue("first_name" in test.validation_errors, "first_name should have validation error %s" % test.validation_errors)


    def test_max__valid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # TODO: 206 set correct number of characters 150
        test.first_name = "Lorem ipsum dolor sit amet, consectetur adipi" # 45 characters

        # act
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")

        self.assertFalse("first_name" in test.validation_errors, "first_name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # TODO: 206 set correct number of characters 150 + 1
        test.first_name = "Lorem ipsum dolor sit amet, consectetur adipis" # 46 characters + 1

        # act
        test.validate()

        # assert
        self.assertTrue("first_name" in test.validation_errors, "first_name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -this model cls_registereduser.RegisterUserModel may not be required")
class test_RegisteredUserModel__validate__last_name(Lesson_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up
        test = self._construct_valid_object()

        test.last_name = "A"
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("last_name" in test.validation_errors, "last_name should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        test.last_name = ""

        # test
        test.validate()

        # assert
        self.assertTrue("last_name" in test.validation_errors, "last_name should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = RegisteredUserModel()

        test.last_name = None

        # test
        test.validate()

        # assert
        self.assertTrue("last_name" in test.validation_errors, "last_name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):

        # arrange
        test = RegisteredUserModel()

        # TODO: 206 set correct number of characters 150
        test.last_name = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("last_name" in test.validation_errors, "last_name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # TODO: 206 set correct number of characters 150 + 1
        test.last_name = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        # test
        test.validate()

        # assert
        self.assertTrue("last_name" in test.validation_errors, "last_name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -this model cls_registereduser.RegisterUserModel may not be required")
class test_RegisteredUserModel__validate__email(Lesson_TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        test.email = "A"
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("email" in test.validation_errors, "email should not have validation error %s" % test.validation_errors)


    def test_min__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        test.email = ""

        # test
        test.validate()

        # assert
        self.assertTrue("email" in test.validation_errors, "email should not have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = RegisteredUserModel()

        test.email = None

        # test
        test.validate()

        # assert
        self.assertTrue("email" in test.validation_errors, "email should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        test = RegisteredUserModel()
        # TODO: 206 set correct number of characters 255
        test.email = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("email" in test.validation_errors, "email should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # TODO: 206 set correct number of characters 255 + 1
        test.email = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa"
        # test
        test.validate()

        # assert
        self.assertTrue("email" in test.validation_errors, "email should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
