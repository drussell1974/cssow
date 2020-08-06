from unittest import TestCase, skip
from shared.models.cls_content import ContentModel as Model


class test_cls_content__validate__description(TestCase):

    test = None

    def setUp(self):
        # start with valid model exept attribute under test
        self.test = Model(1, description = "", letter_prefix = "A")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.description = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("description" in self.test.validation_errors, "description should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme_trim_whitespace(self):
        # set up

        self.test.description = " "

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.description, "")
        self.assertFalse(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.description = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.description = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a condimentum felis. "\
                "Sed et tristique ex, luctus facilisis mauris. Morbi lacinia, ex vitae blandit lobortis, arcu velit fermentum arcu, "\
                "ut placerat odio odio et nisi. Mauris eu dui suscipit, rhoncus lorem eget, porta quam. Maecenas venenatis vulputate auctor. "\
                "Donec metus purus, egestas sed consequat sit amet, consequat sit amet nulla. Sed quis ipsum interdum est dictum efficitur sed "\
                "sed felis. In maximus non arcu efficitur porta dui." # length 500 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("description" in self.test.validation_errors, "description should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a condimentum felis. "\
                "Sed et tristique ex, luctus facilisis mauris. Morbi lacinia, ex vitae blandit lobortis, arcu velit fermentum arcu, "\
                "ut placerat odio odio et nisi. Mauris eu dui suscipit, rhoncus lorem eget, porta quam. Maecenas venenatis vulputate auctor. "\
                "Donec metus purus, egestas sed consequat sit amet, consequat sit Xamet nulla. Sed quis ipsum interdum est dictum efficitur sed "\
                "sed felis. In maximus non arcu efficitur porta dui." # length 501 characters
        # test
        self.test.validate()

        # assert
        self.assertTrue("description" in self.test.validation_errors, "description should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_keyword__validate__letter_prefix(TestCase):

    test = None

    def setUp(self):
        # start with valid model exept attribute under test
        self.test = Model(1
            , description = "Donec metus purus, egestas sed consequat sit amet, consequat sit Xamet nulla. Sed quis ipsum interdum est dictum efficitur sed"
            , letter_prefix = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.letter_prefix = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("letter_prefix" in self.test.validation_errors, "letter_prefix should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.letter_prefix = " X "

        # test
        self.test.validate()

        # assert
        self.assertFalse("letter_prefix" in self.test.validation_errors, "letter_prefix should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.letter_prefix, "X")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.letter_prefix = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.letter_prefix = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.letter_prefix = "Z" # length 1 character

        # test
        self.test.validate()

        # assert
        self.assertFalse("letter_prefix" in self.test.validation_errors, "letter_prefix should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.letter_prefix = "AZ" # length  characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_min__cannot_be_a_number(self):
        # set up

        self.test.letter_prefix = "1"

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__cannot_be_a_specialcharacter(self):
        # set up

        self.test.letter_prefix = "("

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__cannot_be_a_lowercase_character(self):
        # set up

        self.test.letter_prefix = "s"

        # test
        self.test.validate()

        # assert
        self.assertTrue("letter_prefix" in self.test.validation_errors, "letter_prefix should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")

