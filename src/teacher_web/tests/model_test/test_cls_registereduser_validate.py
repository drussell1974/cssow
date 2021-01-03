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

        # set number of characters 150
        test.first_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tristique nisi eros,"\
            "porta tempor elit pharetra eget. Curabitur placerat arcu a et." 

        # act
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")

        self.assertFalse("first_name" in test.validation_errors, "first_name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # set number of characters 150 + 1
        test.first_name = "Lorem ipsumx dolor sit amet, consectetur adipiscing elit. Curabitur tristique nisi eros,"\
            "porta tempor elit pharetra eget. Curabitur placerat arcu a et."

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

        # set number of characters 150
        test.last_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "\
             "Proin in neque ut turpis mollis tincidunt. Nulla eget pulvinar ante. Lorem ipsum dolor nulla."

        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("last_name" in test.validation_errors, "last_name should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # set number of characters 150 + 1
        test.last_name = "Lorem ipsumx dolor sit amet, consectetur adipiscing elit. "\
             "Proin in neque ut turpis mollis tincidunt. Nulla eget pulvinar ante. Lorem ipsum dolor nulla."

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
        # set number of characters 255
        test.email = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel tellus nisl. "\
            "Proin maximus laoreet augue eget pellentesque. Vestibulum venenatis non elit vitae convallis. "\
            "Vestibulum nulla libero, posuere quis dapibus sed, elementum sed risus lectus."
        # test
        test.validate()

        # assert
        self.assertTrue(test.is_valid, "is_valid should be True")
        self.assertFalse("email" in test.validation_errors, "email should not have validation error %s" % test.validation_errors)


    def test_max__invalid_extreme(self):
        # arrange
        test = RegisteredUserModel()

        # set number of characters 255 + 1
        test.email = "Lorem ipsumx dolor sit amet, consectetur adipiscing elit. Maecenas vel tellus nisl. "\
            "Proin maximus laoreet augue eget pellentesque. Vestibulum venenatis non elit vitae convallis. "\
            "Vestibulum nulla libero, posuere quis dapibus sed, elementum sed risus lectus."

        # test
        test.validate()

        # assert
        self.assertTrue("email" in test.validation_errors, "email should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
