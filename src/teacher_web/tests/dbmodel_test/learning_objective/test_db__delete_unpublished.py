from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, LearningObjectiveDataAccess, handle_log_info

delete_unpublished = LearningObjectiveDataAccess.delete_unpublished


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

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = Model(1, "")
        
        expected_result = []

        LearningObjectiveDataAccess._get_lesson_learning_objective_ids = Mock(return_value=[("5654"),("332"),("4545")])

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = delete_unpublished(self.fake_db, 19, auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                'DELETE FROM sow_learning_objective__has__lesson WHERE lesson_id = 19 AND learning_objective_id=4;'
                , log_info=handle_log_info)

            LearningObjectiveDataAccess._get_lesson_learning_objective_ids.assert_called_with(self.fake_db, 19, 99)
