from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_learningobjective import LearningObjectiveModel as Model, handle_log_info

#get_lesson_learning_objective_ids = Model.get_lesson_learning_objective_ids

@skip("NOT USED")
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

            actual_results = get_lesson_learning_objective_ids(self.fake_db, 873, 99)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "CALL lesson_learning_objective__get_learning_objective_ids(873, 99);"
                , []
                , log_info=handle_log_info)
