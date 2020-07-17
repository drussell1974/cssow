from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_reference as testcontext 

get_number_of_resources = testcontext.get_number_of_resources
handle_log_info = testcontext.handle_log_info


class test_db__get_number_of_references(TestCase):
    
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
                get_number_of_resources(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_number_of_resources(self.fake_db, 12, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  lesson_id FROM sow_lesson__has__references WHERE lesson_id = 12;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (34)
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 237, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  lesson_id FROM sow_lesson__has__references WHERE lesson_id = 237;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(1, actual_results)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (45),
            (56),
            (89),
            (90),
            (998)
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 7, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  lesson_id FROM sow_lesson__has__references WHERE lesson_id = 7;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(5, actual_results)