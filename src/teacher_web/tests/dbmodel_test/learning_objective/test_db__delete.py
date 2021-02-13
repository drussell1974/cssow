from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel, handle_log_info
from shared.models.cls_department import DepartmentModel
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

        model = LearningObjectiveModel(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert    
            with self.assertRaises(Exception):
                # act 
                LearningObjectiveModel.delete(self.fake_db, 1, model.id)


    def test_should_call__delete(self, mock_auth_user):
         # arrange
        model = LearningObjectiveModel(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = LearningObjectiveModel.delete(self.fake_db, model, mock_auth_user)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db, 
                "lesson_learning_objective__delete"
                , (101, mock_auth_user.id)
                , handle_log_info)
            
            self.assertEqual(expected_result, actual_result)