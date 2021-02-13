from unittest import TestCase, skip
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_institute__get_options(TestCase):

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
                Model.get_options(self.fake_db, key_stage_id = 4)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_options(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'institute__get_options'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self, mock_auth_user):
        # arrange
        expected_result = [(1,"Computer Science")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_options(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get_options'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual("Computer Science", rows[0].name, "First item not as expected")
            

    def test__should_call__select__multiple_items(self, mock_auth_user):
        # arrange
        expected_result = [(1,"Computer Science"), (2, "Business"), (3, "IT")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_options(self.fake_db, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get_options'
                , (mock_auth_user.id,)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
            self.assertEqual("Computer Science", rows[0].name, "First item not as expected")
            self.assertEqual("IT", rows[len(rows)-1].name, "Last item not as expected")

