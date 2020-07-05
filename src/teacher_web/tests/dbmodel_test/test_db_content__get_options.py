from tests.dbmodel_test._unittest import TestCase, FakeDb
import cls_content as db_content
import db_helper

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
        #self.assertEqual(('SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 1;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual(29, rows[0].id, "First result should be '{}'".format(rows[0].id))
        self.assertEqual(30, rows[1].id, "Second result should be '{}'".format(rows[1].id))
        self.assertEqual(33, rows[len(rows)-2].id, "Second to last result should be '{}'".format(rows[len(rows)-2].id))
        self.assertEqual(34, rows[len(rows)-1].id, "Last result should be '{}'".format(rows[len(rows)-1].id))


    def test__get_options__key_stage_id_2__should_return__8_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=2)
        self.assertEqual(8, len(rows))
        #self.assertEqual(('SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 2;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual(17, rows[0].id, "First result should be '{}'".format(rows[0].id))
        self.assertEqual(35, rows[1].id, "Second result should be '{}'".format(rows[1].id))
        self.assertEqual(40, rows[len(rows)-2].id, "Second to last result should be '{}'".format(rows[len(rows)-2].id))
        self.assertEqual(41, rows[len(rows)-1].id, "Last result should be '{}'".format(rows[len(rows)-1].id))


    def test__get_options__key_stage_id_3__should_return__9_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=3)
        self.assertEqual(9, len(rows))
        #self.assertEqual(('SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 3;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual(42, rows[0].id, "First result should be '{}'".format(rows[0].id))
        self.assertEqual(43, rows[1].id, "Second result should be '{}'".format(rows[1].id))
        self.assertEqual(49, rows[len(rows)-2].id, "Second to last result should be '{}'".format(rows[len(rows)-2].id))
        self.assertEqual(50, rows[len(rows)-1].id, "Last result should be '{}'".format(rows[len(rows)-1].id))


    def test__get_options__key_stage_id_4_should_return__15_records(self):

        rows = db_content.get_options(self.fake_db, key_stage_id=4)
        self.assertEqual(15, len(rows))
        #self.assertEqual(('SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 4;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual(1, rows[0].id, "First result should be '{}'".format(rows[0].id))
        self.assertEqual(2, rows[1].id, "Second result should be '{}'".format(rows[1].id))
        self.assertEqual(14, rows[len(rows)-2].id, "Second to last result should be '{}'".format(rows[len(rows)-2].id))
        self.assertEqual(15, rows[len(rows)-1].id, "Last result should be '{}'".format(rows[len(rows)-1].id))


    def test__get_options__key_stage_id_5_should_return__9_records(self):
        rows = db_content.get_options(self.fake_db, key_stage_id=5)
        self.assertEqual(9, len(rows))
        #self.assertEqual(('SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = 5;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual(19, rows[0].id, "First result should be '{}'".format(rows[0].id))
        self.assertEqual(20, rows[1].id, "Second result should be '{}'".format(rows[1].id))
        self.assertEqual(26, rows[len(rows)-2].id, "Second to last result should be '{}'".format(rows[len(rows)-2].id))
        self.assertEqual(27, rows[len(rows)-1].id, "Last result should be '{}'".format(rows[len(rows)-1].id))
