from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_keyword import KeywordModel
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__publish_by_id(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                KeywordModel.publish_by_id(self.fake_db, 1, 123)


    def test_should_call_update(self, mock_auth_user):
        # arrange
        
        expected_result = [(1,)]

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = KeywordModel.publish_by_id(self.fake_db, 123, mock_auth_user)
            
            # assert
            ExecHelper.update.assert_called_with(self.fake_db,
                "keyword__publish"
                , (123, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , handle_log_info)
            
            self.assertEqual(1, len(actual_result))

