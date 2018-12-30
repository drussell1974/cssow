from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_topic
import db_helper

class test_db_topic__get_options__level_1(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__get_options__invalid_extreme__explicity_pass_None__should_return__nothing(self):
        #test
        rows = db_topic.get_options(self.fake_db, topic_id=None, lvl = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__get_options_topic_0__should_return_nothing(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=0, lvl = 1)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 1 AND (id  = 0 or parent_id = 0 or related_topic_id = 0);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Algorithms", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_1__should_return_6(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=1, lvl = 1)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 1 AND (id  = 1 or parent_id = 1 or related_topic_id = 1);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Algorithms", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_6__should_return_6(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=6, lvl = 1)
        # assert
        self.assertEqual(6, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE lvl = 1 AND (id  = 6 or parent_id = 6 or related_topic_id = 6);', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Algorithms", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_topic_7__should_return_nothing(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=7, lvl = 1)
        # assert
        self.assertEqual(0, len(rows))


    def test__get_options_topic_72__should_return_nothing(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=72, lvl = 1)
        # assert
        self.assertEqual(0, len(rows))



