from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info
#get_key_words = LessonModel.get_key_words

@skip
class test_db__get_key_words__dict(TestCase):
    
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
                get_key_words(self.fake_db, 21)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_key_words(self.fake_db, 67)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT kw.id as id, kw.name as name FROM sow_key_word as kw INNER JOIN sow_lesson__has__key_words as lkw ON kw.id = lkw.key_word_id WHERE lesson_id = 67;"
                , []
                , log_info=handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [("87","Fetch Decode Execute")]
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_key_words(self.fake_db, 87)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT kw.id as id, kw.name as name FROM sow_key_word as kw INNER JOIN sow_lesson__has__key_words as lkw ON kw.id = lkw.key_word_id WHERE lesson_id = 87;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual("Fetch Decode Execute", actual_results["87"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [("1034","DDR"),("1045","DIMM"),("12","DRAM") ]
        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_key_words(self.fake_db, 21)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                " SELECT kw.id as id, kw.name as name FROM sow_key_word as kw INNER JOIN sow_lesson__has__key_words as lkw ON kw.id = lkw.key_word_id WHERE lesson_id = 21;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual("DDR", actual_results["1034"])
            self.assertEqual("DRAM", actual_results["12"])
