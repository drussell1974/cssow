from unittest import TestCase
from shared.models.cls_year import YearModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from tests.test_helpers.mocks import fake_ctx_model

#@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_YearDataAccess__get_options(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self):
        # arrange

        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_options(self.fake_db, key_stage_id = 4)
            

    def test__should_call__select__no_items(self):
        # arrange

        mock_auth_user = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_options(self.fake_db, key_stage_id = 1, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'year__get_options'
                , (1, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self):
        # arrange

        mock_auth_user = fake_ctx_model()
        
        expected_result = [(1,"Yr4")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_options(self.fake_db, key_stage_id = 2, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'year__get_options'
                , (2, 6079)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual("Yr4", rows[0].name, "First item not as expected")
            

    def test__should_call__select__multiple_items(self):
        # arrange

        mock_auth_user = fake_ctx_model()

        expected_result = [(1,"Yr7"), (2, "Yr8"), (3, "Yr9")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_options(self.fake_db, key_stage_id = 3, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'year__get_options'
                , (3, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))
            self.assertEqual("Yr7", rows[0].name, "First item not as expected")
            self.assertEqual("Yr9", rows[len(rows)-1].name, "Last item not as expected")

