from datetime import datetime
from unittest import TestCase
from shared.models.core.basemodel import try_int


class test_cls_basemodel_try_int(TestCase):

    test = None
    created_now = datetime.now()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__retain_int(self):
        result = try_int(1)
        self.assertEqual(1, result)


    def test__convert_int_string_to_int(self):
        result = try_int("1")
        self.assertEqual(1, result)


    def test__convert_character_string_to_null(self):
        result = try_int("A")
        self.assertEqual(None, result)


    def test__convert_none_to_none(self):
        result = try_int(None)
        self.assertEqual(None, result)
