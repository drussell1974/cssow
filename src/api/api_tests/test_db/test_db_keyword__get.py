from unittest import TestCase, skip
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import cls_keyword as db_keyword
import db_helper

class test_db_keyword__get_options(TestCase):
    def setUp(self):
        self.ids = []
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()


    def tearDown(self):
        for id in self.ids:
            db_keyword.delete(self.fake_db, id)

        self.fake_db.close()


    def test__get__single_keyword(self):
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["something"]))
        rows = db_keyword.get_by_terms(self.fake_db, "something", True)
        self.assertTrue(1, len(rows))


    def test__get__multiple_keyword(self):
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["something"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["or"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["nothing"]))

        rows = db_keyword.get_by_terms(self.fake_db, "something,or,nothing", True)
        self.assertEqual(3, len(rows))


    @skip('check keywords functionality')
    def test__empty_string__show_all(self):

        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["something"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["or"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["nothing"]))

        rows = db_keyword.get_by_terms(self.fake_db, "", True)
        self.assertEqual(31, len(rows))


    def test__empty_string__do_not_show_all(self):

        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["something"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["or"]))
        self.ids.append(db_keyword.save_keywords_only(self.fake_db, ["nothing"]))

        rows = db_keyword.get_by_terms(self.fake_db, "", False)
        self.assertEqual(0, len(rows))
