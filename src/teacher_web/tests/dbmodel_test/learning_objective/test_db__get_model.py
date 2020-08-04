from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context

# test context

get_model = test_context.LearningObjectiveModel.get_model
handle_log_info = test_context.handle_log_info


class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 99, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, le.id as lesson_id, sow.key_stage_id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.notes as notes, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  lob.published as published  FROM sow_scheme_of_work as sow INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE lob.id = 99 AND (lob.published = 1 or lob.created_by = 1);"
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, actual_results.id)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            321,"Understanding numbering systems",
            3,"Unistructural", 4, 12,
            "State the different numbering systems", 45,
            3, "KS3",
            "Binary,Denary,Hexadecimal", "Revise the names three different numbering systems",
            "Theory", "2020-07-17 02:12:34", 1, "test_user", 1
        )]
        
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, auth_user=1)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lob.id as id, lob.description as description, solo.id as solo_id, solo.name as solo_taxonomy_name, solo.lvl as solo_taxonomy_level, cnt.id as content_id, cnt.description as content_description, le.id as lesson_id, sow.key_stage_id as key_stage_id, ks.name as key_stage_name, lob.key_words as key_words, lob.notes as notes, lob.group_name as group_name, lob.created as created, lob.created_by as created_by_id, CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  lob.published as published  FROM sow_scheme_of_work as sow INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id LEFT JOIN auth_user as user ON user.id = lob.created_by WHERE lob.id = 321 AND (lob.published = 1 or lob.created_by = 1);"
                , []
                , log_info=handle_log_info)
            

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.description)
            self.assertEqual("Unistructural", actual_results.solo_taxonomy_name)
            self.assertEqual("State the different numbering systems", actual_results.content_description)
            self.assertEqual("Binary,Denary,Hexadecimal", actual_results.key_words)
            self.assertEqual("Revise the names three different numbering systems", actual_results.notes)


