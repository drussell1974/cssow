from unittest import TestCase


# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from db_helper import from_db_bool

class test__db_helper__to_db_bool(TestCase):


    def test__should_change_True_to_1(self):
        result = from_db_bool(1)

        self.assertEqual(True, result)


    def test__should_change_False_to_0(self):
        result = from_db_bool(0)

        self.assertEqual(False, result)
