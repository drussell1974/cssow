import shared.models.cls_examboard as test_context
from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info

get_options = test_context.ExamBoardModel.get_options


class test_db_exam_board__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        test_context.handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                test_context.get_options(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_exam_board;', [], test_context.handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(123, "Item 1")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_exam_board;', [], test_context.handle_log_info)
            self.assertEqual(1, len(rows))
            self.assertEqual(123, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(1, "Item 1"),(2,"Item 2"),(3, "Item 3")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            rows = get_options(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_exam_board;', [], test_context.handle_log_info)
            
            self.assertEqual(3, len(rows))

            self.assertEqual(1, rows[0].id)
            self.assertEqual("Item 1", rows[0].name)

            self.assertEqual(3, rows[2].id)
            self.assertEqual("Item 3", rows[2].name)
