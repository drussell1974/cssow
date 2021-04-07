from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_notification import NotifyModel as Model, NotifyModelDataAccess
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__delete(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.delete(db=self.fake_db, event_log_id=12832746, auth_ctx=mock_ctx)


    def test_should_call__delete(self, mock_ctx):
        # arrange
        
        expected_result = 2001

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(db=self.fake_db, event_log_id=12832746, auth_ctx=mock_ctx)

            # assert
            
            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "logging_notification__delete"
                , (12832746, mock_ctx.auth_user_id)
            )

            # check subsequent functions where called

            self.assertEqual(2001, actual_result)
           