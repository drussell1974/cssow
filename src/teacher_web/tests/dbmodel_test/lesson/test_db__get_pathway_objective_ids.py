from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_lesson as cls_lesson 

handle_log_info = cls_lesson.handle_log_info
get_pathway_objective_ids = cls_lesson.get_pathway_objective_ids

class test_db__get_pathway_objective_ids(TestCase):
    
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
                get_pathway_objective_ids(self.fake_db, 21)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_pathway_objective_ids(self.fake_db, 67)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT learning_objective_id FROM sow_lesson__has__pathway WHERE lesson_id = 67;"
                , [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [("87")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_pathway_objective_ids(self.fake_db, 87)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT learning_objective_id FROM sow_lesson__has__pathway WHERE lesson_id = 87;"
            , [])

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [("1034"),("1045"),("12") ]


        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_pathway_objective_ids(self.fake_db, 21)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT learning_objective_id FROM sow_lesson__has__pathway WHERE lesson_id = 21;"
                , [])
            
            self.assertEqual(1034, actual_results[0])
            self.assertEqual(12, actual_results[2])
