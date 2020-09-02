from unittest import TestCase, skip
from shared.models.cls_keyword import KeywordModel


class test_cls_keyword__validate__definition(TestCase):

    test = None

    def setUp(self):
        self.test = KeywordModel(1, term = "A", definition = "", scheme_of_work_id=13)


    def tearDown(self):
        pass


    def test_min__valid(self):
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


class test_cls_keyword__validate__term(TestCase):

    test = None

    def setUp(self):
        self.test = KeywordModel(1, "", "", scheme_of_work_id=13)


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

        self.test.term = "Vivamus leo massae feugiat venenatis urna ute venenatis rutrum massae Mauris vel justo nisl Quisquez" # length 100 characters

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


    def test__cannot_be_non_alphanumeric_only(self):
        # set up

        self.test.term = ","

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test__cannot_start_with_comma(self):
        # set up

        self.test.term = ",AAAA"

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test__cannot_start_with_special_characters(self):
        # set up

        self.test.term = "&AAAA"

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test__cannot_include_special_characters(self):
        # set up

        self.test.term = "AAdfA!"

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test__should_not_be_number_only(self):
        # set up

        self.test.term = "99"

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")



    def test__can_contain_a_number(self):
        # set up

        self.test.term = "9A"

        # test
        self.test.validate()

        # assert
        self.assertTrue("term" in self.test.validation_errors, "term should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_should_be_valid(self):

        for word in ["ABCVDFas df2", "A1234", "ABCVDFas", "A9", "A9B", "A 10", "ABC (DEF)"]:
            self.test.term = word
            # test
            self.test.validate()
            self.assertTrue("term" not in self.test.validation_errors, "value '{}' should be valid".format(word))


    def test_should_not_be_valid(self):

        for word in ["9ABCVDFas df2", "99", " 101", "99 " "9A", "ABCVD,Fasd,JUErE", "A,1,2,3", "1,2,3", "34343434A", ";", "a;", "A{}"]:
            self.test.term = word
            # test
            self.test.validate()
            self.assertTrue("term" in self.test.validation_errors, "value '{}' should not be valid".format(word))


class test_cls_keyword__validate__scheme_of_work_id(TestCase):

    test = None

    def setUp(self):
        self.test = KeywordModel(1, term = "A", definition = "", scheme_of_work_id=13)


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # set up

        self.test.scheme_of_work_id = 1

        # test
        self.test.validate()

        # assert
        self.assertFalse("scheme_of_work_id" in self.test.validation_errors, "scheme_of_work_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # set up

        self.test.scheme_of_work_id = 0

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in self.test.validation_errors, "scheme_of_work_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test_max__valid_extreme(self):
        # set up
        
        self.test.scheme_of_work_id = 99999

        # test
        self.test.validate()

        # assert
        self.assertFalse("scheme_of_work_id" in self.test.validation_errors, "scheme_of_work_id should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # set up

        self.test.scheme_of_work_id = 100000

        # test
        self.test.validate()

        # assert
        self.assertTrue("scheme_of_work_id" in self.test.validation_errors, "scheme_of_work_id should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "is_valid should be False")
