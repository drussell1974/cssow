from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_institute__get_model(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_model(self.fake_db, 5034, mock_auth_user)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            act_result = Model.get_model(self.fake_db, 5034, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'institute__get'
                , (5034, mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertFalse(act_result.is_from_db)
            self.assertFalse(act_result.is_valid)
            

    def test__should_call__select__item(self, mock_auth_user):
        # arrange
        expected_result = [(1, "Computer Science", 539, "2020-07-21 17:09:34", 1, "test_user", 0)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            act_result = Model.get_model(self.fake_db, 5034, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get'
                , (5034, mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual("Computer Science", act_result.name, "First item not as expected")
