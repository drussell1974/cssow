from unittest import TestCase
from shared.models.cls_keyword import KeywordModel


class test_cls_keyword__validate__definition(TestCase):

    test = None

    def setUp(self):
        self.test = KeywordModel(1, term = "A", definition = "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.definition = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("definition" in self.test.validation_errors, "definition should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.definition = " "

        # test
        self.test.validate()

        # assert
        self.assertFalse("definition" in self.test.validation_errors, "definition should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.definition, "")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme(self):
        # set up

        self.test.definition = ""

        # test
        self.test.validate()

        # assert
        self.assertFalse("definition" in self.test.validation_errors, "definition should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should not be is_valid")


    def test_min__valid_extreme_when_None(self):
        # set up

        self.test.definition = None

        # test
        self.test.validate()

        # assert
        self.assertFalse("definition" in self.test.validation_errors, "definition should have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.definition = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverr. " # length 250 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("definition" in self.test.validation_errors, "definition should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.definition = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in viverra urna. " \
                          "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. " \
                          "Quisque quis risus id ligula tempor pellentesque at at neque. Ut sed viverra. " # length 251 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("definition" in self.test.validation_errors, "definition should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


class test_cls_reference__validate__term(TestCase):

    test = None

    def setUp(self):
        self.test = KeywordModel(1, "", "")


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.term = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("term" in self.test.validation_errors, "term should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.term = " x "

        # test
        self.test.validate()

        # assert
        self.assertFalse("term" in self.test.validation_errors, "term should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.term, "x")
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.term = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.term = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # set up

        self.test.term = "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. Quisque" # length 100 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("term" in self.test.validation_errors, "term should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.term = "Vivamus leo massa, feugiat venenatis urna ut, venenatis rutrum massa. Mauris vel justo nisl. Quisques" # length 101 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
