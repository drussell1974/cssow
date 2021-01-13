from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info

delete_unpublished = Model.delete_unpublished


class test_db__delete_unpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call__delete(self):
        # arrange
        
        expected_result = []

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act
            
            delete_unpublished(self.fake_db, 13, 19, auth_user=99)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db, 
                "lesson_learning_objective__delete_unpublished"
                , (13, 19,99)
                , handle_log_info)
