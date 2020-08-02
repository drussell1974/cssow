from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, LearningObjectiveDataAccess, handle_log_info

update_is_key_objective = LearningObjectiveDataAccess.update_is_key_objective

@skip("Deprecated. Not implemented.")
class test_db__update_is_key_objective(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                update_is_key_objective(self.fake_db, [])


    def test__should_call_execSql(self):
        # arrange

        model = Model(34, lesson_id = 84)
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=[]):
            # act

            actual_results = update_is_key_objective(self.fake_db, 34, 84, [])

            # assert

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db,
                "UPDATE sow_learning_objective__has__lesson SET is_key_objective = 0 WHERE learning_objective_id = 34;"
                , log_info=handle_log_info)


