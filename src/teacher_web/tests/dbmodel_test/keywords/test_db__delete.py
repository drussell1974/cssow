from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__delete(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, term="Morbi", definition="sit amet mauris ut ante porttitor interdum.")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.delete(self.fake_db, model, mock_auth_user)


    def test_should_call__delete(self, mock_auth_user):
        # arrange
        model = Model(797, term="Morbi", definition="sit amet mauris ut ante porttitor interdum.", scheme_of_work_id = 12)
        
        expected_result = 1

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(self.fake_db, model, mock_auth_user)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db, 
             'keyword__delete'
             , (797, 12, mock_auth_user.auth_user_id)
             , handle_log_info)
            
            self.assertEqual(expected_result, actual_result)