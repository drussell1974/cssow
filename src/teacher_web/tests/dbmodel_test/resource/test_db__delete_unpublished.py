from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_resource import ResourceModel, handle_log_info

# Test Context

delete_unpublished = ResourceModel.delete_unpublished


class test_db__delete_unpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call_execCRUDSql(self):
         # arrange
        
        expected_result = 5

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = delete_unpublished(self.fake_db, 1, auth_user=99)
            
            # assert
            ExecHelper.execSql.assert_called()

            ExecHelper.execSql.assert_called_with(self.fake_db, 
                "DELETE FROM sow_resource WHERE lesson_id = 1 AND published = 0;"
                , []
                , handle_log_info)

            self.assertEqual(expected_result, actual_result)
