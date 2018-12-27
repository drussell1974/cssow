from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_content


class test_db_content__get_options(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__get_options__key_stage_id_0__should_return__nothing(self):

        rows = db_content.get_options(self.fake_db, key_stage_id=0)
        self.assertEqual(0, len(rows))


    def test__get_options__key_stage_id_1__should_return__6_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=1)
        self.assertEqual(6, len(rows))


    def test__get_options__key_stage_id_2__should_return__8_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=2)
        self.assertEqual(8, len(rows))


    def test__get_options__key_stage_id_3__should_return__9_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=3)
        self.assertEqual(9, len(rows))


    def test__get_options__key_stage_id_4_should_return__15_records(self):

        rows = db_content.get_options(self.fake_db, key_stage_id=4)
        self.assertEqual(15, len(rows))


    def test__get_options__key_stage_id_5_should_return__9_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=5)
        self.assertEqual(9, len(rows))
