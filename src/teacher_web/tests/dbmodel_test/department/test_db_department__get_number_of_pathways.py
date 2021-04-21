from unittest import TestCase
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_DepartmentDataAccess__get_number_of_pathways(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__scalar__with_exception(self, mock_ctx):

        # arrange
        expected_result = KeyError('Bang')
        
        with patch.object(ExecHelper, "scalar", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                Model.get_number_of_pathways(self.fake_db, department_id=67, auth_user=mock_ctx)
            

    def test__should_call__scalar__no_items(self, mock_ctx):
        # arrange
        expected_result = (0,)

        with patch.object(ExecHelper, "scalar", return_value=expected_result):
                
            # act
            
            result = Model.get_number_of_pathways(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                'department__get_number_of_pathways'
                , []
                , handle_log_info
                , (12776111277611, mock_ctx.auth_user_id,))

            self.assertEqual(0, result)


    def test__should_call__scalar__single_items(self, mock_ctx):
        # arrange
        expected_result = (1,)
        
        with patch.object(ExecHelper, "scalar", return_value=expected_result):
            
            # act

            rows = Model.get_number_of_pathways(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db, 
                'department__get_number_of_pathways'
                , []
                , handle_log_info
                , (12776111277611, mock_ctx.auth_user_id,))


            self.assertEqual(1, rows)
            

    def test__should_call__scalar__multiple_items(self, mock_ctx):
        # arrange
        expected_result = (3,)

        with patch.object(ExecHelper, "scalar", return_value=expected_result):
            # act
            rows = Model.get_number_of_pathways(self.fake_db, 12776111277611, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db, 
                'department__get_number_of_pathways'
                , []
                , handle_log_info
                , (12776111277611, mock_ctx.auth_user_id,))
            
            self.assertEqual(3, rows)
