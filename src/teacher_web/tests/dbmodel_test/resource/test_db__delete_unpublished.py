from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_resource import ResourceModel, handle_log_info
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__delete_unpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                ResourceModel.delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call_delete(self, mock_auth_user):
         # arrange
        
        expected_result = 5

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = ResourceModel.delete_unpublished(self.fake_db, 1, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db, 
                "lesson_resource__delete_unpublished"
                , (1, mock_auth_user.id)
                , handle_log_info)

            self.assertEqual(expected_result, actual_result)
