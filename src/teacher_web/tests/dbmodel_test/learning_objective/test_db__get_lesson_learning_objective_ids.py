from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_learningobjective as test_context

# test context

Model = test_context.LearningObjectiveModel
_get_lesson_learning_objective_ids = test_context._get_lesson_learning_objective_ids
handle_log_info = test_context.handle_log_info

class test_db___get_lesson_learning_objective_ids(TestCase):
    

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
                _get_lesson_learning_objective_ids(self.fake_db, [])


    def test__should_call_execSql__return_no_rows(self):
        # arrange

        expected_results = []

        model = Model(74, lesson_id = 15)
        
        with patch.object(ExecHelper, 'execSql', return_value=[]):
            # act

            actual_results = _get_lesson_learning_objective_ids(self.fake_db, 873, [])

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lol.learning_objective_id FROM sow_learning_objective__has__lesson AS lol INNER JOIN sow_lesson AS l ON l.id = lol.lesson_id INNER JOIN sow_learning_objective AS lo ON lo.id = lol.learning_objective_id WHERE lo.published = 0 AND l.id=873 AND l.created_by = [];"
                , []
                , log_info=handle_log_info)


