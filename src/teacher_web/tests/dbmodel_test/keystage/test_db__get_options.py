from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_keystage as testcontext 

get_options = testcontext.get_options
handle_log_info = testcontext.handle_log_info


class test_db__get_options(TestCase):
    
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
                get_options(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id, name FROM sow_key_stage;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (4, "KS4")
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id, name FROM sow_key_stage;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(4, rows[0].id)
            self.assertEqual("KS4", rows[0].name)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (3, "KS3"),
            (4, "KS4"),
            (5, "KS5")
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id, name FROM sow_key_stage;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(3, rows[0].id)
            self.assertEqual("KS3", rows[0].name)

            self.assertEqual(5, rows[2].id)
            self.assertEqual("KS5", rows[2].name)