from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_topic
import db_helper

class test_db_topic__get_options__level_2(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__get_options__invalid_extreme__explicity_pass_None__should_return__nothing(self):
        #test
        rows = db_topic.get_options(self.fake_db, topic_id=None, lvl = 2)
        # assert
        self.assertEqual(0, len(rows))


    def test__get_options_topic_0__should_return_nothing(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=0, lvl = 2)
        # assert
        self.assertEqual(0, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 2 AND (id  = 0 or parent_id = 0 or related_topic_id = 0);', 'SUCCESS'), db_helper.last_sql)
        #self.assertEqual("Computing", rows[0].name, "First result should be {}".format(rows[0].name))
        #self.assertEqual("Algorithms", rows[1].name, "Second result should be {}".format(rows[1].name))
        #self.assertEqual("Communication and networks", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        #self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_1__should_return_7(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=1, lvl = 2)
        # assert
        self.assertEqual(7, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 2 AND (id  = 1 or parent_id = 1 or related_topic_id = 1);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Problem solving", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Boolean algebra", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_6__should_return_12(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=6, lvl = 2)
        # assert
        self.assertEqual(12, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 2 AND (id  = 6 or parent_id = 6 or related_topic_id = 6);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Internet services", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Environment", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_7__should_return_8(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=7, lvl = 2)
        # assert
        self.assertEqual(8, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 2 AND (id  = 7 or parent_id = 7 or related_topic_id = 7);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("CPU", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Optical storage", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_72__should_return_X(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=72, lvl = 2)
        # assert
        self.assertEqual(12, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 2 AND (id  = 72 or parent_id = 72 or related_topic_id = 72);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Internet services", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Environment", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))



