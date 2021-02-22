from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel, SchemeOfWorkModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__deleteunpublished(TestCase):


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

        model = SchemeOfWorkModel(0, auth_user=mock_auth_user)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                SchemeOfWorkModel.delete_unpublished(self.fake_db, 1)


    def test_should_call__delete(self, mock_auth_user):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=(5)):
            # act

            actual_result = SchemeOfWorkModel.delete_unpublished(self.fake_db, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db,
                'scheme_of_work__delete_unpublished'
                , (0, mock_auth_user.auth_user_id)
                , handle_log_info)

            self.assertEqual(5, actual_result)
