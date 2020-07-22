from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_lesson as cls_lesson 

handle_log_info = cls_lesson.handle_log_info
get_all_keywords = cls_lesson.LessonDataAccess.get_all_keywords

class test_db__get_all_keywords(TestCase):
    
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
                get_all_keywords(self.fake_db, 21)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all_keywords(self.fake_db, 67)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT kw.id as id, name as term, definition as definition FROM sow_lesson__has__key_words lkw INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id WHERE lkw.lesson_id = 67 AND published = 1;"
                , []
                , log_info=handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange

        with patch.object(ExecHelper, 'execSql', return_value=[(87,"Fetch Decode Execute", "The process carried out by the CPU")]):
            # act

            actual_results = get_all_keywords(self.fake_db, 87)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT kw.id as id, name as term, definition as definition FROM sow_lesson__has__key_words lkw INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id WHERE lkw.lesson_id = 87 AND published = 1;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0].id)
            self.assertEqual("Fetch Decode Execute", actual_results[0].term)
            self.assertEqual("The process carried out by the CPU", actual_results[0].definition)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange

        with patch.object(ExecHelper, 'execSql', return_value=[(1034,"DDR",""),(1045,"DIMM",""),(12,"DRAM","") ]):
            # act

            actual_results = get_all_keywords(self.fake_db, 21)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT kw.id as id, name as term, definition as definition FROM sow_lesson__has__key_words lkw INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id WHERE lkw.lesson_id = 21 AND published = 1;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual("DDR", actual_results[0].term)
            self.assertEqual("DRAM", actual_results[2].term)
