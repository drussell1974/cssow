from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_resource import ResourceModel, handle_log_info
from tests.test_helpers.mocks import *

# TODO: #329 remove global refernence
get_number_of_resources = ResourceModel.get_number_of_resources

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_number_of_resources(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_scalar__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'scalar', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_number_of_resources(self.fake_db, 99, auth_user=99)


    def test__should_call_scalar__return_no_items(self, mock_ctx):
        # arrange
        expected_result = [0]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act
            
            actual_results = get_number_of_resources(self.fake_db, 677, auth_user=mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                'lesson__get_number_of_resources'
                , []
                , handle_log_info
                , (677,1,mock_ctx.auth_user_id))

            self.assertEqual(0, actual_results)


    def test__should_call_scalar__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [1]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 12, auth_user=mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , []
                , handle_log_info
                , (12,1,mock_ctx.auth_user_id)
                )
            
            self.assertEqual(1, actual_results)


    def test__should_call_scalar__return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [3]

        with patch.object(ExecHelper, 'scalar', return_value=expected_result):
            # act

            actual_results = get_number_of_resources(self.fake_db, 22, auth_user=mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                "lesson__get_number_of_resources"
                , []
                , handle_log_info
                , (22, 1, mock_ctx.auth_user_id)
                )
            
            self.assertEqual(3, actual_results)
