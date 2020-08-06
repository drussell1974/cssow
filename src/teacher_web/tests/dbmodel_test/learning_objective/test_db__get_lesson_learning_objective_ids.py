from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info

get_lesson_learning_objective_ids = Model.get_lesson_learning_objective_ids


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
                get_lesson_learning_objective_ids(self.fake_db, [])


    def test__should_call_execSql__return_no_rows(self):
        # arrange

        expected_results = []

        model = Model(74, lesson_id = 15)
        
        with patch.object(ExecHelper, 'execSql', return_value=[]):
            # act

            actual_results = get_lesson_learning_objective_ids(self.fake_db, 873, [])

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT lol.learning_objective_id FROM sow_learning_objective__has__lesson AS lol INNER JOIN sow_lesson AS l ON l.id = lol.lesson_id INNER JOIN sow_learning_objective AS lo ON lo.id = lol.learning_objective_id WHERE lo.published = 0 AND l.id=873 AND l.created_by = [];"
                , []
                , log_info=handle_log_info)
