from unittest import TestCase, skip
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
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
                Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 0)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            test_keywords = "algorithms,abstract"
            result = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE pw.lesson_id = 72 ORDER BY ks.name DESC, solo.lvl;", [])

            self.assertEqual(0, len(result))


    def test__should_call_execSql_return_single_item(self):
        # arrange    
        expected_result = [(1, "a", 2, "b", 3, 4, "c" ,5 , "d" ,"e" ,"f" ,"g" ,6 ,"h")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            
            # test
            test_keywords = "algorithms,abstract"
            rows = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db, "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE pw.lesson_id = 72 ORDER BY ks.name DESC, solo.lvl;", [])

            self.assertEqual(1, len(rows), "number of linked pathways should 1")
            ' first item '
            self.assertEqual(1, rows[0].id, "first item not as expected")
            self.assertEqual("a", rows[0].description)
         

    def test__should_call_execSql_return_mutliple_items(self):
        # arrange
        expected_result = [(1, "a", 2, "b", 3, 4, "c" ,5 , "d" ,"e" ,"f" ,"g" ,6 ,"h"),
                       (7, "aa", 8, "ab", 9, 10, "ac" ,11 , "ad" ,"ae" ,"af" ,"ag" ,12 ,"ah"),
                        (13, "ba", 14, "bb", 15, 16, "bc" ,17 , "bd" ,"be" ,"bf" ,"bg" ,18 ,"bh")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            
            # act
            test_keywords = "algorithms,abstract"
            result = Model.get_linked_pathway_objectives(self.fake_db, lesson_id = 72)

            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,  "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, ks.id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name FROM sow_learning_objective as lob INNER JOIN sow_lesson__has__pathway as pw ON pw.learning_objective_id = lob.id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN sow_key_stage as ks ON ks.id = cnt.key_stage_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE pw.lesson_id = 72 ORDER BY ks.name DESC, solo.lvl;", [])

            self.assertEqual(3, len(result), "number of linked pathways should 3")
            ' first item '
            self.assertEqual(1, result[0].id, "first item not as expected")
            self.assertEqual("a", result[0].description)


            self.assertEqual(13, result[2].id, "last item not as expected")
            self.assertEqual("ba", result[2].description)