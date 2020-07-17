from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_lesson as cls_lesson

LessonModel = cls_lesson.LessonModel
_upsert_pathway_ks123_ids = cls_lesson._upsert_pathway_ks123_ids
handle_log_info = cls_lesson.handle_log_info

class test_db__upsert_pathway_ks123_ids(TestCase):


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
                _upsert_pathway_ks123_ids(self.fake_db, model, auth_user_id=99)


    def test_should_call_execCRUDSql__delete_only__when__no_pathway_ks123_ids(self):
         # arrange
        model = LessonModel(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = _upsert_pathway_ks123_ids(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson__has__ks123_pathway WHERE lesson_id = 101;"
             , []
             , log_info=handle_log_info)

        self.assertEqual(actual_result, expected_result)
    
    
    def test_should_call_execCRUDSql__reinsert__pathway_ks123_ids(self):
         # arrange
        model = LessonModel(10, "")
        model.pathway_ks123_ids = ["201","202"]
        expected_result = []

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = _upsert_pathway_ks123_ids(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "INSERT INTO sow_lesson__has__ks123_pathway (lesson_id, ks123_pathway_id) VALUES(10, 201),(10, 202);"
             , []
             , log_info=handle_log_info)

        self.assertEqual(actual_result, expected_result)
    