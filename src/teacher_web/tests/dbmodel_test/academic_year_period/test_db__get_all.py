from unittest import TestCase
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_academic_year_period import AcademicYearPeriodModel as Model
from shared.models.enums.publlished import STATE
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_AcademicYearPeriodDataAccess__get_all(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange

        #mock_ctx = fake_ctx_model()
        
        expected_result = KeyError('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                Model.get_all(self.fake_db, mock_auth_user.institute_id, auth_ctx=mock_auth_user)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange

        #mock_ctx = fake_ctx_model()

        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act00
            
            rows = Model.get_all(self.fake_db, mock_auth_user.institute_id, auth_ctx = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'academic_year_period__get_all'
                , (mock_auth_user.institute_id, mock_auth_user.selected_year, mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self, mock_auth_user):
        # arrange

        #mock_ctx = fake_ctx_model()
        
        expected_result = [("08:30","Period 1")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_all(self.fake_db, mock_auth_user.institute_id, auth_ctx = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'academic_year_period__get_all'
                , (mock_auth_user.institute_id, mock_auth_user.selected_year, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)


            self.assertEqual(1, len(rows))
            self.assertEqual("08:30", rows[0].time)
            self.assertEqual("Period 1", rows[0].name)
            

    def test__should_call__select__multiple_items(self, mock_auth_user):
        # arrange

        #mock_ctx = fake_ctx_model()

        expected_result = [
            ("08:30","Period 1"),
            ("09:30","Period 2"),   
            ("11:00","Period 3"),
        ]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_all(self.fake_db, mock_auth_user.institute_id, auth_ctx = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'academic_year_period__get_all'
                , (mock_auth_user.institute_id, mock_auth_user.selected_year, mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            
            self.assertEqual(3, len(rows))
            self.assertEqual("08:30", rows[0].time)
            self.assertEqual("Period 1", rows[0].name)
            self.assertEqual("11:00", rows[2].time)
            self.assertEqual("Period 3", rows[2].name)
