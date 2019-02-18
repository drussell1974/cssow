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

        db_keyword.delete(self.fake_db, "something")
        db_keyword.delete(self.fake_db, "or")
        db_keyword.delete(self.fake_db, "nothing")


    def tearDown(self):
        self.fake_db.close()


    def test__get__single_keyword(self):
        db_keyword.save(self.fake_db, ["something"])
        rows = db_keyword.get(self.fake_db, "something")
        self.assertTrue(1, len(rows))


    def test__get__multiple_keyword(self):
        db_keyword.save(self.fake_db, ["something"])
        db_keyword.save(self.fake_db, ["or"])
        db_keyword.save(self.fake_db, ["nothing"])

        rows = db_keyword.get(self.fake_db, "something,or,nothing")
        self.assertEqual(3, len(rows))
