from unittest import TestCase

from db_helper import to_db_bool

class test__db_helper__to_db_bool(TestCase):


    def test__should_change_True_to_1(self):
        result = to_db_bool(True)

        self.assertEqual(1, result)


    def test__should_change_False_to_0(self):
        result = to_db_bool(False)

        self.assertEqual(0, result)
