from unittest import TestCase, skip
from shared.models.cls_department import DepartmentModel as Model, handle_log_info
from shared.models.enums.publlished import STATE
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_department__get_my(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):

        # arrange
        expected_result = KeyError('Bang')
        
        with patch.object(ExecHelper, "select", side_effect=expected_result):
            # act and assert
            with self.assertRaises(KeyError):
                Model.get_my(self.fake_db, institute=mock_auth_user.institute, department_id=mock_auth_user.department_id, auth_user = mock_auth_user)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department_id=mock_auth_user.department.id, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 'department__get_my$2'
                , (mock_auth_user.institute.id, mock_auth_user.department.id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    @patch.object(Model, "get_number_of_schemes_of_work", return_value=12)
    def test__should_call__select__single_items(self, DepartmentModel_get_number_of_schemes_of_work, mock_auth_user):
        # arrange
        expected_result = [(1, "Computer Science", 3, "2020-07-21 17:09:34", 1, "test_user", 0)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department_id=mock_auth_user.department.id, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'department__get_my$2'
                , (mock_auth_user.institute.id, mock_auth_user.department.id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            DepartmentModel_get_number_of_schemes_of_work.assert_called_with(self.fake_db, 1, mock_auth_user)

            self.assertEqual(1, len(rows))
            self.assertEqual("Computer Science", rows[0].name, "First item not as expected")
            

    @patch.object(Model, "get_number_of_schemes_of_work", return_value=111)
    def test__should_call__select__multiple_items(self, DepartmentModel_get_number_of_schemes_of_work, mock_auth_user):
        # arrange
        expected_result = [
            (1, "Computer Science", 3, "2020-07-21 17:09:34", 1, "test_user", 0),
            (2, "Business", 2, "2020-07-21 17:09:34", 1, "test_user", 1), 
            (3, "IT", 1, "2020-07-21 17:09:34", 1, "test_user", 1)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department_id=mock_auth_user.department.id, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'department__get_my$2'
                , (mock_auth_user.institute.id, mock_auth_user.department.id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            DepartmentModel_get_number_of_schemes_of_work.assert_called()

            self.assertEqual(3, len(rows))
            
            self.assertEqual("Computer Science", rows[0].name)
            self.assertEqual(3, rows[0].topic_id)

            self.assertEqual("IT", rows[len(rows)-1].name)
            self.assertEqual(1, rows[len(rows)-1].topic_id)

