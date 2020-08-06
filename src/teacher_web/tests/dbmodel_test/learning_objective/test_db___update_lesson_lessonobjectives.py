from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_learningobjective import LearningObjectiveModel as Model, LearningObjectiveDataAccess, handle_log_info

_update_lesson_lessonobjectives = LearningObjectiveDataAccess._update_lesson_lessonobjectives


class test_db___update_lesson_lessonobjectives(TestCase):
    

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
                _update_lesson_lessonobjectives(self.fake_db, [])


    def test__should_call_execSql(self):
        # arrange

        model = Model(74, lesson_id = 15)
        
        with patch.object(ExecHelper, 'execCRUDSql', return_value=[]):
            # act

            actual_results = _update_lesson_lessonobjectives(self.fake_db, model, [])

            # assert

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db,
                "INSERT INTO sow_learning_objective__has__lesson (learning_objective_id, lesson_id) VALUES (74, 15);"
                , log_info=handle_log_info)


