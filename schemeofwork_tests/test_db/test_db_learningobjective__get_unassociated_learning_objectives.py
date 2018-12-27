from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_learningobjective


class test_db_content__get_options(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__all_zeros__should_return_zero_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives( self.fake_db, learning_episode_id=0, key_stage_id=0, topic_id=0)
        self.assertEqual(0, len(rows))

    def test__key_stage_4__should_return_1_records(self):
        rows = db_learningobjective.get_unassociated_learning_objectives(self.fake_db, learning_episode_id=60, key_stage_id=4, topic_id=1)
        self.assertEqual(1, len(rows))
