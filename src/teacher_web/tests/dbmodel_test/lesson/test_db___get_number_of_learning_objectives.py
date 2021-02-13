from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_number_of_learning_objectives(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mockauth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                Model.get_number_of_learning_objectives(self.fake_db, 21, auth_user=6079)


    def test__should_call_select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = [(0,)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_results = Model.get_number_of_learning_objectives(self.fake_db, 67, auth_user=mock_ctx)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_learning_objectives"
                , (67, mock_ctx.user_id)
                , []
                , handle_log_info)

            self.assertEqual(0, actual_results)


    def test__should_call_select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [(1,)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = Model.get_number_of_learning_objectives(self.fake_db, 87, auth_user=mock_ctx)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
            "lesson__get_number_of_learning_objectives"
            , (87, mock_ctx.user_id)
            , []
            , handle_log_info)

            self.assertEqual(1, actual_results)


    def test__should_call_select__return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [(3,)]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = Model.get_number_of_learning_objectives(self.fake_db, 21, auth_user=mock_ctx)

            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "lesson__get_number_of_learning_objectives"
                , (21, mock_ctx.user_id)
                , []
                , handle_log_info)
            
            self.assertEqual(3, actual_results)
