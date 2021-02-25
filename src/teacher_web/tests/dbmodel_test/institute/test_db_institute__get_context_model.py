from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel, InstituteContextModel as Model, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import fake_ctx_model

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_institute__get_context_model(TestCase):

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
                Model.get_context_model(self.fake_db, 5034, mock_auth_user)
            

    def test__should_call__select__no_item(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, "select", return_value=expected_result):
                
            # act
            
            act_result = Model.get_context_model(self.fake_db, 5034, auth_user_id = mock_auth_user.id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'institute__get_context_model'
                , (5034,)
                , None
                , handle_log_info)

            self.assertEqual(0, act_result.id)
            self.assertEqual("", act_result.name)
            #self.assertEqual(None, model.parent_id)
            self.assertEqual(0, act_result.created_by_id)
            self.assertEqual(int(STATE.PUBLISH), act_result.published)
            self.assertEqual("published", act_result.published_state)
            
            
    @patch.object(InstituteModel, "get_number_of_departments", return_value=12)
    def test__should_call__select__item(self, InstituteModel_get_number_of_departments, mock_auth_user):
        # arrange
        expected_result = [(15, "Computer Science", 539, 101, 4)]
        
        with patch.object(ExecHelper, "select", return_value=expected_result):
            
            # act

            act_result = Model.get_context_model(self.fake_db, 5034, auth_user_id = mock_auth_user.id)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db, 
                'institute__get_context_model'
                , (5034,)
                , None
                , handle_log_info)

            self.assertEqual(15, act_result.id)
            self.assertEqual("Computer Science", act_result.name)
            #self.assertEqual(None, model.parent_id)
            self.assertEqual(101, act_result.created_by_id)
            self.assertEqual(int(STATE.PUBLISH_INTERNAL), act_result.published)
            self.assertEqual("published", act_result.published_state)

