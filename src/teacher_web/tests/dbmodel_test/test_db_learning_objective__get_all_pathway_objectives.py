from ._unittest import TestCase, FakeDb
from unittest import skip
from shared.models.cls_learningobjective import LearningObjectiveDataAccess, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from unittest import skip
from shared.models.core.db_helper import ExecHelper


class test_db_learning_objective__get_pathway_objectives(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        handle_log_info = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                LearningObjectiveDataAccess.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words="test1,test2")


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            test_keywords = ","
            result = LearningObjectiveDataAccess.get_all_pathway_objectives(self.fake_db, key_stage_id = 0, key_words=test_keywords)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 0 ORDER BY ks.name DESC, solo.lvl;", [])
            self.assertEqual(0, len(result))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(1,"understand how to pass this test", 2, "describe, identify", 3, 4,"content here",5,"KS4","mouse,keyboard","Group 1","Dave",6,"today", "abc", "abstraction")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            test_keywords = "algorithm,abstraction"
            result = LearningObjectiveDataAccess.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 5 ORDER BY ks.name DESC, solo.lvl;", [])
            self.assertEqual(1, len(result))
            ' first item '
            self.assertEqual(1, result[0]["id"], "first item not as expected")
            self.assertEqual("understand how to pass this test", result[0]["description"])


    def test__should_call_execSql_return_multiple_items(self):
        # arrange
        
        test_keywords = "algorithm,abstract,abstraction"
        
        expected_result = [
            (1,"Give the names of different components for a PC", 2, "describe, identify", 3, 4,"content here",5,"KS4","mouse,keyboard","Group 1","Dave",6,"today", "abc", "abstraction"),
            (7,"Describe the purpose of the CPU", 8, "explain, justify", 9, 10,"provide some detail",10,"KS4","CPU,RAM","Group 1","Dave",11,"yesterday", "algorithm", "abstraction"),
            (12,"Explain the difference between RISC and CISC and justify reason for using them", 13, "explain, justify", 14, 15,"include higher level questions",16,"KS4","RISC,CISC","Group 1","Dave",1,"yesterday", "algorithm", "abstraction")
            ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            result = LearningObjectiveDataAccess.get_all_pathway_objectives(self.fake_db, key_stage_id = 5, key_words=test_keywords)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,"SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob LEFT JOIN sow_topic as top ON top.id = lob.topic_id LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE ks.id < 5 ORDER BY ks.name DESC, solo.lvl;", [])
            self.assertEqual(3, len(result))
            ' first item '
            self.assertEqual(1, result[0]["id"], "first item not as expected")
            self.assertEqual("Give the names of different components for a PC", result[0]["description"])
            ' last item '
            self.assertEqual(12, result[2]["id"], "first item not as expected")
            self.assertEqual("Explain the difference between RISC and CISC and justify reason for using them", result[2]["description"])
