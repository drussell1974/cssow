from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info

_upsert_pathway_objective_ids = LessonDataAccess._upsert_pathway_objective_ids


class test_db__upsert_pathway_objective_ids(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                _upsert_pathway_objective_ids(self.fake_db, model)


    def test_should_call_execCRUDSql__delete_only__when__no__pathway_objective_ids(self):
         # arrange
        model = LessonModel(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = _upsert_pathway_objective_ids(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson__has__pathway WHERE lesson_id = 101;"
             , []
             , log_info=handle_log_info)
            
        self.assertEqual(expected_result, actual_result)


    def test_should_call_execCRUDSql__reinsert__pathway_objective_ids(self):
         # arrange
        model = LessonModel(1043, "")
        model.pathway_objective_ids = ["12","13","14"]
        expected_result = []

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = _upsert_pathway_objective_ids(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "INSERT INTO sow_lesson__has__pathway (lesson_id, learning_objective_id) VALUES(1043, 12),(1043, 13),(1043, 14);"
             , []
             , log_info=handle_log_info)
            
        self.assertEqual(expected_result, actual_result)
