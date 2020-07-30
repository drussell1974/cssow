from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_learningobjective as test_context

Model = test_context.LearningObjectiveModel
delete = test_context.LearningObjectiveDataAccess.delete
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

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete(self.fake_db, 1, model.id)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete(self.fake_db, 1, model.id)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_learning_objective__has__lesson WHERE learning_objective_id = 101;"
             , log_info=handle_log_info)
            
            self.assertEqual(expected_result, actual_result)