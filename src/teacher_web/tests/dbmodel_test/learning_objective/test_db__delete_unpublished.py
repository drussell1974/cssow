from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__delete_unpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.delete_unpublished(self.fake_db, 1, auth_user=mock_auth_user)


    def test_should_call__delete(self, mock_auth_user):
        # arrange
        
        expected_result = []

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act
            
            Model.delete_unpublished(self.fake_db, 13, 19, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db, 
                "lesson_learning_objective__delete_unpublished"
                , (13, 19, mock_auth_user.auth_user_id)
                , handle_log_info)
