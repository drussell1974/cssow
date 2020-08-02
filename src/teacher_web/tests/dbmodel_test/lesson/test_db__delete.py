from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info

delete = LessonDataAccess._delete

class test_db__delete(TestCase):


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
                delete(self.fake_db, 1, model)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = LessonModel(101, "")
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=model):
            # act

            actual_result = delete(self.fake_db, 1, model)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson WHERE id = 101 AND published IN (0,2);"
             , []
             , log_info=handle_log_info)
            
            self.assertEqual(101, actual_result.id)