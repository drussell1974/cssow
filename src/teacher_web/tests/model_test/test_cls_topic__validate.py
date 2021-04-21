from unittest import TestCase, skip
from shared.models.cls_topic import TopicModel
from tests.test_helpers.mocks import *


class test_cls_topic__validate__name(TestCase):

    test = None

    def setUp(self):
        with patch("shared.models.core.django_helper", return_value=fake_ctx_model()) as mock_auth_user:
            self.test = TopicModel(1, name = "A", auth_ctx=mock_auth_user)


    def tearDown(self):
        pass


    def test_min__valid(self):
        # set up

        self.test.name = "A"

        # test
        self.test.validate()

        # assert
        self.assertFalse("name" in self.test.validation_errors, "name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid)


    def test_min__valid_extreme_trim_whitespace(self):
        # set up

        self.test.name = " A "

        # test
        self.test.validate()

        # assert
        self.assertFalse("name" in self.test.validation_errors, "name should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.name, "A")
        self.assertTrue(self.test.is_valid)


    def test_min__invalid(self):
        # set up

        self.test.name = ""

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid)


    def test_min__invalid_extreme_trim_whitespace(self):
        # set up

        self.test.name = " "

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should have no validation errors - %s" % self.test.validation_errors)
        self.assertEqual(self.test.name, "")
        self.assertFalse(self.test.is_valid)


    def test_min__invalid_extreme_when_None(self):
        # set up

        self.test.name = None

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid)


    def test_max__valid_extreme(self):
        # set up

        self.test.name = "Lorem ipsum dolor sit amet, consectetur nisi." # length 45 characters

        # test
        self.test.validate()

        # assert
        self.assertFalse("name" in self.test.validation_errors, "name should not have validation error %s" % self.test.validation_errors)
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur nisi.", self.test.name)
        self.assertTrue(self.test.is_valid)


    def test_max__invalid_extreme(self):
        # set up

        self.test.name = "Lorem ipsum dolor sit amet, consectetur nisix." # length 46 characters

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should have validation error %s" % self.test.validation_errors)
        self.assertEqual("Lorem ipsum dolor sit amet, consectetur nisix.", self.test.name)
        self.assertFalse(self.test.is_valid)


@skip("not implemented yet - could be a good idea - see keyword for use of _validate_duplicate")
class test_cls_keyword__validate__name__duplicate_check(TestCase):

    test = None

    def setUp(self):
        self.test = TopicModel(0, "", department_id=13)


    def tearDown(self):
        pass


    def test__name__when_unique___if_new(self):
        
        # set up
        self.test.name = "A"
        self.test.all_topic_names = ["B", "C", "D"]

        # test
        self.test.validate()

        # assert
        self.assertFalse("name" in self.test.validation_errors, "name should not have validation error %s" % self.test.validation_errors)
        self.assertTrue(self.test.is_valid, "should be is_valid")


    def test__when_duplicate___if_new(self):

        # set up
        self.test.name = "A"
        self.test.all_topic_names = ["A", "B", "C"]

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")


    def test__when_duplicate___if_not_new(self):

        # set up
        self.test.id = 1
        self.test.name = "A"
        self.test.all_topic_names = ["A", "B", "C"]

        # test
        self.test.validate()

        # assert
        self.assertTrue("name" in self.test.validation_errors, "name should not have validation error %s" % self.test.validation_errors)
        self.assertFalse(self.test.is_valid, "should not be is_valid")
