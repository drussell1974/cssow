from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_learningobjective
import db_helper

class test_db_content__get_options(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def dtest__all_zeros__should_return_zero_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives( self.fake_db, learning_episode_id=0, key_stage_id=0, topic_id=0)
        self.assertEqual(' ks.id = 0 AND top.id = 0 AND (le.id != 0 OR le_lo.learning_objective_id is null) ORDER BY top.name;', db_helper.last_sql[0].split('WHERE')[1])
        self.assertEqual('SUCCESS', db_helper.last_sql[1])
        self.assertEqual(0, len(rows))


    def test__key_stage_3__KS3_COMPUTING_1__should_return_1_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives(self.fake_db, learning_episode_id=58, key_stage_id=3, topic_id=10)
        self.assertEqual(1, len(rows))
        self.assertEqual(' ks.id = 3 AND top.id = 10 AND (le.id != 58 OR le_lo.learning_objective_id is null) ORDER BY top.name;', db_helper.last_sql[0].split('WHERE')[1])
        self.assertEqual('SUCCESS', db_helper.last_sql[1])

        self.assertEqual(466, rows[0].id, "First result should be '{}'".format(rows[0].id))


    def test__key_stage_3__KS3_COMPUTING_2__should_return_0_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives(self.fake_db, learning_episode_id=70, key_stage_id=3, topic_id=10)
        self.assertEqual(1, len(rows))
        self.assertEqual(' ks.id = 3 AND top.id = 10 AND (le.id != 70 OR le_lo.learning_objective_id is null) ORDER BY top.name;', db_helper.last_sql[0].split('WHERE')[1])
        self.assertEqual('SUCCESS', db_helper.last_sql[1])
        #467
        self.assertEqual(0, rows[0].id, "First result should be '{}'".format(rows[0].id))


    def test__key_stage_4__should_return_1_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives(self.fake_db, learning_episode_id=60, key_stage_id=4, topic_id=1)
        self.assertEqual(1, len(rows))
        self.assertEqual(' ks.id = 4 AND top.id = 1 AND (le.id != 60 OR le_lo.learning_objective_id is null) ORDER BY top.name;', db_helper.last_sql[0].split('WHERE')[1])
        self.assertEqual('SUCCESS', db_helper.last_sql[1])

        self.assertEqual(411, rows[0].id, "First result should be '{}'".format(rows[0].id))


