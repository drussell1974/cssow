from datetime import datetime
from _unittest import TestCase
from basemodel import BaseModel

class Test_basemodel_Constructor(TestCase):

    test = None
    created_now = datetime.now()

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_validate_for_default_instance_returns_false(self):

        # setup
        test = BaseModel(0,
                        created = self.created_now,
                        created_by_id = 1,
                        created_by_name = "Dave Russell",
                        published = 0)

        # test
        test.validate()

        # validate
        self.assertFalse(test.is_valid)


    def test_constructor_default(self):

        # test
        test = BaseModel(0,
                        created = self.created_now,
                        created_by_id = 1,
                        created_by_name = "Dave Russell",
                        published = 0)

        # assert
        self.assertEqual(0, test.id)
        self.assertEqual(False, test.is_valid, "is_valid should be False")
        self.assertTrue(len(test.validation_errors) == 0)


    def test_constructor_set_valid_values(self):

        # setup

        test = BaseModel(id_=1,
                        created = self.created_now,
                        created_by_id = 1,
                        created_by_name = "Dave Russell",
                        published = 0)

        # test
        test.validate()

        # assert
        self.assertEqual(1, test.id)
        self.assertEqual(self.created_now, test.created)
        self.assertEqual(1, test.created_by_id)
        self.assertFalse(test.is_valid, "is_valid should be False")
        self.assertTrue(len(test.validation_errors) == 0, "%s" % test.validation_errors)

    def test_constructor_is_new(self):

        # test
        test = BaseModel(0,
                        created = self.created_now,
                        created_by_id = 1,
                        created_by_name = "Dave Russell",
                        published = 0)

        # assert
        self.assertEqual(0, test.id)
        self.assertTrue(test.is_new())

    def test_constructor_NOT_is_new(self):

        # test
        test = BaseModel(1,
                        created = self.created_now,
                        created_by_id = 1,
                        created_by_name = "Dave Russell",
                        published = 0)

        # assert
        self.assertEqual(1, test.id)
        self.assertFalse(test.is_new())
