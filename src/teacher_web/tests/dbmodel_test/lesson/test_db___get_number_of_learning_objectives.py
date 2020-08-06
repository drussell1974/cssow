from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_lesson import LessonModel, handle_log_info


get_number_of_learning_objectives = LessonModel.get_number_of_learning_objectives


class test_db__get_number_of_learning_objectives(TestCase):
    
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
                get_number_of_learning_objectives(self.fake_db, 21, auth_user=99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_number_of_learning_objectives(self.fake_db, 67, auth_user=99)

            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  id FROM sow_learning_objective__has__lesson WHERE lesson_id = 67;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [("87",)]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_number_of_learning_objectives(self.fake_db, 87, auth_user=99)

            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  id FROM sow_learning_objective__has__lesson WHERE lesson_id = 87;"
            , []
            , log_info=handle_log_info)

            self.assertEqual(1, actual_results)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [("1034",),("1045",),("12",)]


        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_number_of_learning_objectives(self.fake_db, 21, auth_user=99)

            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  id FROM sow_learning_objective__has__lesson WHERE lesson_id = 21;"
                , []
                , log_info=handle_log_info)
            
            self.assertEqual(3, actual_results)
