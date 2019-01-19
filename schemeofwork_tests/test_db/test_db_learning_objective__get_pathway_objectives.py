from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_learningobjective

class test_db_learning_objective__get_pathway_objectives(TestCase):
    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()

    def test_return_nothing_when_empty_topics(self):
        # test
        result = db_learningobjective.get_pathway_objectives(self.fake_db, key_stage_id = 0, topic_ids = "", key_words="test")

        # assert
        self.assertTrue(len(result) == 0)


    def test_return_nothing_when_empty_keywords(self):
        # test
        result = db_learningobjective.get_pathway_objectives(self.fake_db, key_stage_id = 0, topic_ids = "0", key_words="")

        # assert
        self.assertTrue(len(result) == 0)
