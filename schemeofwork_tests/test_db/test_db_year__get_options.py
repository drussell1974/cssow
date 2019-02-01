from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_year
import db_helper

class test_db_year__get_options__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__key_stage_1__should_return_3_items(self):
        # test
        rows = db_year.get_options(self.fake_db, key_stage_id = 1)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Yr1", rows[0].name, "First item not as expected")
        self.assertEqual("Yr3", rows[len(rows)-1].name, "Last item not as expected")


    def test__key_stage_2__should_return_3_items(self):
        # test
        rows = db_year.get_options(self.fake_db, key_stage_id = 2)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Yr4", rows[0].name, "First item not as expected")
        self.assertEqual("Yr6", rows[len(rows)-1].name, "Last item not as expected")


    def test__key_stage_3__should_return_3_items(self):
        # test
        rows = db_year.get_options(self.fake_db, key_stage_id = 3)
        # assert
        self.assertEqual(3, len(rows))
        self.assertEqual("Yr7", rows[0].name, "First item not as expected")
        self.assertEqual("Yr9", rows[len(rows)-1].name, "Last item not as expected")


    def test__key_stage_4__should_return_2_items(self):
        # test
        rows = db_year.get_options(self.fake_db, key_stage_id = 4)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Yr10", rows[0].name, "First item not as expected")
        self.assertEqual("Yr11", rows[len(rows)-1].name, "Last item not as expected")


    def test__key_stage_5__should_return_2_items(self):
        # test
        rows = db_year.get_options(self.fake_db, key_stage_id = 5)
        # assert
        self.assertEqual(2, len(rows))
        self.assertEqual("Yr12", rows[0].name, "First item not as expected")
        self.assertEqual("Yr13", rows[len(rows)-1].name, "Last item not as expected")

