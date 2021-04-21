from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel, DepartmentContextModel as Model, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_DepartmentDataAccess__get_context_model(TestCase):

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
                Model.get_context_model(self.fake_db)
            

    def test__should_call__select__no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            act_result = Model.get_context_model(self.fake_db, department_id=999, institute_id=127671276711, auth_user_id = mock_auth_user.auth_user_id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'department__get_context_model$2'
                , (127671276711, 999)
                , None
                , handle_log_info)

            self.assertEqual(0, act_result.id)
            self.assertEqual("", act_result.name)
            #self.assertEqual(None, model.parent_id)
            self.assertEqual(0, act_result.created_by_id)
            self.assertEqual(32, act_result.published)
            self.assertEqual("unpublished", act_result.published_state)

            
    @patch.object(DepartmentModel, "get_number_of_schemes_of_work", return_value=3)
    def test__should_call__select__items(self, DepartmentModel_get_number_of_schemes_of_work, mock_auth_user):
        # arrange
        expected_result = [(593,"Computer Science", 3, 12776111277611, 99, 1)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            act_result = Model.get_context_model(self.fake_db, department_id=593, institute_id=127671276711,  auth_user_id = mock_auth_user.auth_user_id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'department__get_context_model$2'
                , (127671276711, 593,)
                , None
                , handle_log_info)
                
            self.assertEqual(593, act_result.id)
            self.assertEqual("Computer Science", act_result.name)
            #self.assertEqual(None, model.parent_id)
            self.assertEqual(99, act_result.created_by_id)
            self.assertEqual(int(STATE.PUBLISH), act_result.published)
            self.assertEqual("published", act_result.published_state)
