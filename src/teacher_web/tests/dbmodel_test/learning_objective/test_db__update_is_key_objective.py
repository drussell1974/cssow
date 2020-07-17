from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context

# test context

Model = test_context.LearningObjectiveModel
update_is_key_objective = test_context.update_is_key_objective
handle_log_info = test_context.handle_log_info

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


