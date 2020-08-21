from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_learningobjective as test_context

Model = test_context.LearningObjectiveModel
delete = test_context.LearningObjectiveModel.delete
handle_log_info = test_context.handle_log_info

class test_db__delete(TestCase):


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
                delete(self.fake_db, 1, model.id)


    def test_should_call__delete(self):
         # arrange
        model = Model(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, model, 99)
            
            # assert
            ExecHelper.delete.assert_called_with(self.fake_db, 
                "lesson_learning_objective__delete"
                , (101,99)
                , handle_log_info)
            
            self.assertEqual(expected_result, actual_result)