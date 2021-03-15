from unittest import TestCase, skip
from shared.models.cls_department import DepartmentModel 
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model, handle_log_info
from shared.models.enums.publlished import STATE
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_my(TestCase):

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
                Model.get_my(self.fake_db, institute=mock_auth_user.institute, department=mock_auth_user.department, auth_user = mock_auth_user)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department=mock_auth_user.department, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 'scheme_of_work__get_my'
                , (mock_auth_user.department.id, mock_auth_user.department.institute_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call__select__single_items(self, mock_auth_user):
        # arrange
        expected_result = [
            (1, "Computer Science", "", 3, "AQA", 5, "KS5", "2020-07-21 17:09:34", 1, "test_user", 2, 5, "Computer Science", 2, "Lorem Ipsum"),
        ]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department=mock_auth_user.department, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'scheme_of_work__get_my'
                , (mock_auth_user.department.id, mock_auth_user.department.institute_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(1, len(rows))
            self.assertEqual("Computer Science", rows[0]["name"], "First item not as expected")
            

    def test__should_call__select__multiple_items(self, mock_auth_user):
        # arrange
        expected_result = [
            (1, "Computer Science", "", 3, "AQA", 4, "KS4", "2020-07-21 17:09:34", 1, "test_user", 2, 5, "Computer Science", 2, "Lorem Ipsum"),
            (2, "Business", "", 3, "AQA", 5, "KS5",  "2020-07-21 17:09:34", 1, "test_user", 2, 5, "Computer Science", 2, "Lorem Ipsum"), 
            (3, "IT", "", 3, "AQA", 3, "KS3", "2020-07-21 17:09:34", 1, "test_user", 2, 5, "Computer Science", 2, "Lorem Ipsum")]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            # act
            rows = Model.get_my(self.fake_db, institute=mock_auth_user.institute, department=mock_auth_user.department, auth_user = mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'scheme_of_work__get_my'
                , (mock_auth_user.department.id, mock_auth_user.department.institute_id, int(STATE.PUBLISH), mock_auth_user.auth_user_id,)
                , []
                , handle_log_info)

            self.assertEqual(3, len(rows))
            self.assertEqual("Computer Science", rows[0]["name"], "First item not as expected")
            self.assertEqual("IT", rows[len(rows)-1]["name"], "Last item not as expected")

