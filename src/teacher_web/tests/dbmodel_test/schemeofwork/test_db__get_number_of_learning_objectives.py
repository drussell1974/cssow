from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

# TODO: #329 remove global reference
get_number_of_learning_objectives = SchemeOfWorkModel.get_number_of_learning_objectives


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_number_of_learning_objectives(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_number_of_learning_objectives(self.fake_db, 101, int(STATE.PUBLISH), mock_auth_user)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = get_number_of_learning_objectives(self.fake_db, 101, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_number_of_learning_objectives'
                , (101, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, actual_result)


    def test__should_call__select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(1,)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_result = get_number_of_learning_objectives(self.fake_db, 6, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'scheme_of_work__get_number_of_learning_objectives'
                , (6, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(1, actual_result)



