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


    def test__should_call_select__with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_number_of_learning_objectives(self.fake_db, 21, auth_user=99)


    def test__should_call_select__return_no_items(self):
        # arrange
        expected_result = [(0,)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = get_number_of_learning_objectives(self.fake_db, 67, auth_user=99)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_learning_objectives"
                , (67,99)
                , []
                , handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_select__return_single_item(self):
        # arrange
        expected_result = [(1,)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_number_of_learning_objectives(self.fake_db, 87, auth_user=99)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
            "lesson__get_number_of_learning_objectives"
            , (87,99)
            , []
            , handle_log_info)

            self.assertEqual(1, actual_results)


    def test__should_call_select__return_multiple_item(self):
        # arrange
        expected_result = [(3,)]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_number_of_learning_objectives(self.fake_db, 21, auth_user=99)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_learning_objectives"
                , (21,99)
                , []
                , handle_log_info)
            
            self.assertEqual(3, actual_results)
