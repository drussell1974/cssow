from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
import shared.models.cls_lesson as cls_lesson

LessonModel = cls_lesson.LessonModel
_copy_objective_ids = cls_lesson._copy_objective_ids
handle_log_info = cls_lesson.handle_log_info


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

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                _copy_objective_ids(self.fake_db, model, auth_user_id=99)


    def test_should_not_call_execCRUDSql__delete_only__when__no_related_topic_ids(self):
         # arrange
        model = LessonModel(101, "")
        model.copy()

        expected_result = []

        objectives_to_copy = []

        # preselect
        with patch.object(ExecHelper, 'execSql', return_value=objectives_to_copy):
            # insert
            with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
                # act

                actual_result = _copy_objective_ids(self.fake_db, model, [], auth_user_id=99)
                
                # assert

                ExecHelper.execSql.assert_called_with(self.fake_db, 
                "SELECT learning_objective_id FROM sow_learning_objective__has__lesson WHERE lesson_id = 101;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(actual_result, expected_result)
    
    
    def test_should_call_execCRUDSql__reinsert__related_topic_ids(self):
         # arrange
        model = LessonModel(10, "")
        model.related_topic_ids = ["201","202"]
        expected_result = []

        objectives_to_copy = [("1"),("2"),("99"),("100")]

        # preselect
        with patch.object(ExecHelper, 'execSql', return_value=objectives_to_copy):
            # insert
            with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
                # act

                actual_result = _copy_objective_ids(self.fake_db, model, [], auth_user_id=99)
                
                # assert

                ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
                "INSERT INTO sow_learning_objective__has__lesson (lesson_id, learning_objective_id) VALUES(10, 1),(10, 2),(10, 9),(10, 1);"
                , []
                , log_info=handle_log_info)

            self.assertEqual(actual_result, expected_result)
    