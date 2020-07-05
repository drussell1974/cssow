from tests.model_test._unittest import TestCase, FakeDb
from unittest import skip
import cls_learningobjective as db_learningobjective

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
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words=test_keywords)

        # assert
        self.assertEqual(0, len(result))


    def test_return_nothing_when_list_is_empty_strings(self):
        # test
        test_keywords = ","
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words=test_keywords)

        # assert
        self.assertEqual(0, len(result))


    @skip('check keywords functionality')
    def test_when_keywords_single_keyword(self):
        # test
        test_keywords = "algorithm"
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords)

        # assert
        self.assertEqual(1, len(result))


    
    @skip('check keywords functionality')
    def test_when_multiple_keyword(self):
        # test
        test_keywords = "algorithm,abstract,abstraction"
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords)

        # assert
        self.assertEqual(3, len(result))


    @skip('check keywords functionality')
    def test_when_multiple_keywords_duplicate(self):
        # test
        test_keywords = "algorithm,abstract,algorithm"
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords)

        # assert
        self.assertEqual(3, len(result), "should be 3")


    @skip('check keywords functionality')
    def test_return_results_only_for_previous_key_stages(self):
        # test
        test_keywords = "algorithm,abstract"
        result = db_learningobjective.get_all_pathway_objectives(self.fake_db, key_stage_id = 3, key_words=test_keywords)

        # assert
        self.assertEqual(2, len(result))
