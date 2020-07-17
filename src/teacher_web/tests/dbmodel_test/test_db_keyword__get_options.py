from ._unittest import TestCase, FakeDb
import shared.models.cls_keyword as db_keyword
from unittest.mock import Mock, MagicMock, patch
from unittest import skip
from shared.models.core.db_helper import ExecHelper


class test_db_keyword__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        db_keyword.handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                db_keyword.get_options(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = db_keyword.get_options(self.fake_db)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_key_word kw WHERE published = 1 ORDER BY name;', [])
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(123, "Binary")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = db_keyword.get_options(self.fake_db)
            
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_key_word kw WHERE published = 1 ORDER BY name;', [])
            self.assertEqual(1, len(rows))
            self.assertEqual("Binary", rows[0][1])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(1, "Binary"),(2,"Decimal"),(3, "Hexadecimal")]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = db_keyword.get_options(self.fake_db)
            # assert
            ExecHelper.execSql.assert_called_with(self.fake_db,'SELECT id, name FROM sow_key_word kw WHERE published = 1 ORDER BY name;', [])
            self.assertEqual(3, len(rows))
            self.assertEqual((1, "Binary"), rows[0])
            self.assertEqual((3, "Hexadecimal"), rows[2])
