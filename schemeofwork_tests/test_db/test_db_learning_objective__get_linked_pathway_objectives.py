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


    def test_return_nothing_when_empty_keywords(self):
        # test
        test_keywords = ""
        result = db_learningobjective.get_linked_pathway_objectives(self.fake_db, learning_episode_id = 0)

        # assert
        self.assertEqual(0, len(result))


    def test_return_results(self):
        # test
        test_keywords = "algorithms,abstract"
        result = db_learningobjective.get_linked_pathway_objectives(self.fake_db, learning_episode_id = 35)

        # assert
        self.assertEqual(3, len(result))
