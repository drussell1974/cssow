from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_topic
import db_helper

class test_db_topic__get_options(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__get_options__invalid_extreme__inexplicity_pass_None__should_return__nothing(self):
        # test
        rows = db_topic.get_options(self.fake_db)
        # assert
        self.assertEqual(0, len(rows))

    def test__get_options__invalid_extreme__explicity_pass_None__should_return__nothing(self):
        #test
        rows = db_topic.get_options(self.fake_db, topic_id=None, parent_topic_id=None)
        # assert
        self.assertEqual(0, len(rows))


    def test__get_options__valid_extreme__topic_id_only__should_return__everything(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id = 0)
        # assert
        self.assertEqual(1, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 0 or parent_id = null;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Computing", rows[0].name, "First result should be {}".format(rows[0].name))
        #self.assertEqual("Computing", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_level_0__valid_extreme__min_should_everything(self):
        # test
        rows = db_topic.get_options(self.fake_db, topic_id=0, parent_topic_id=0)
        # assert
        self.assertEqual(7, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 0 or parent_id = 0;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Computing", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Algorithms", rows[1].name, "Second result should be {}".format(rows[1].name))
        self.assertEqual("Communication and networks", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_level_1__valid_extreme__min__should_return__X_records(self):
        rows = db_topic.get_options(self.fake_db, topic_id=1, parent_topic_id=0)
        self.assertEqual(6, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 1 or parent_id = 0;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Algorithms", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Programming and development", rows[1].name, "Second result should be {}".format(rows[1].name))
        self.assertEqual("Communication and networks", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options_level_1__valid_extreme__max__should_return__X_records(self):
        rows = db_topic.get_options(self.fake_db, topic_id=6, parent_topic_id=0)
        self.assertEqual(6, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 6 or parent_id = 0;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Algorithms", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Programming and development", rows[1].name, "Second result should be {}".format(rows[1].name))
        self.assertEqual("Communication and networks", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        self.assertEqual("Information technology", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options__level_2__valid_extreme__min__should_return__X_records(self):
        rows = db_topic.get_options(self.fake_db, topic_id=7, parent_topic_id=4)
        self.assertEqual(8, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 7 or parent_id = 4;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("CPU", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Memory", rows[1].name, "Second result should be {}".format(rows[1].name))
        self.assertEqual("Magnetic storage", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        self.assertEqual("Optical storage", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))


    def test__get_options__level_2__valid_extreme__max__should_return__X_records(self):
        rows = db_topic.get_options(self.fake_db, topic_id=72, parent_topic_id=6)
        self.assertEqual(12, len(rows))
        self.assertEqual(('SELECT DISTINCT id, name, created, created_by FROM view_child_parent_topics WHERE id  = 72 or parent_id = 6;', 'SUCCESS'), db_helper.last_sql)
        self.assertEqual("Internet services", rows[0].name, "First result should be {}".format(rows[0].name))
        self.assertEqual("Programs and applications", rows[1].name, "Second result should be {}".format(rows[1].name))
        self.assertEqual("Artificial Intelligence", rows[len(rows)-2].name, "Second to last result should be {}".format(rows[len(rows)-2].name))
        self.assertEqual("Environment", rows[len(rows)-1].name, "Last result should be {}".format(rows[len(rows)-1].name))
