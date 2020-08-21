from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info

_copy_objective_ids = LessonDataAccess._copy_objective_ids


class test_db___upsert_related_topic_ids(TestCase):


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

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                _copy_objective_ids(self.fake_db, model, auth_user=6079)

    
    
    def test_should_call_insert__to_copy_objectives_ids(self):
         # arrange
        model = Model(10, "")
        expected_result = []

        # insert
        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = _copy_objective_ids(self.fake_db, model, [], auth_user=6079)
            
            # assert

            ExecHelper.insert.assert_called_with(self.fake_db, 
            'lesson__copy_learning_objectives'
            , (10, 0, 6079)
            , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    