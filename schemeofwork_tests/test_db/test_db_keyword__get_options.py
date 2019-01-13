from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_keyword
import db_helper

class test_db_keyword__get_options(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__get_options__should_return__something(self):
        db_keyword.save(self.fake_db, ["something"])
        rows = db_keyword.get_options(self.fake_db)
        self.assertTrue(len(rows) > 0)

