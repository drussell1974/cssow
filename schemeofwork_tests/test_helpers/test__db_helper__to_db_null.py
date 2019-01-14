from unittest import TestCase


# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
from db_helper import to_db_null

class test__db_helper__to_db_null(TestCase):

    def test__should_retain_empty(self):
        result = to_db_null('')

        self.assertEqual('', result)

    def test__should_change_none_to_null(self):
        result = to_db_null(None)

        self.assertEqual('NULL', result)



    def test__should_retain_string(self):
        result = to_db_null("Hello World")

        self.assertEqual('Hello World', result)


    def test__should_retain_int(self):
        result = to_db_null(0)

        self.assertEqual(0, result)


    def test__should_retain_float(self):
        result = to_db_null(0.1)

        self.assertEqual(0.1, result)
