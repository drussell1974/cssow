from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
import shared.models.cls_lesson as cls_lesson

LessonModel = cls_lesson.LessonModel
publish = cls_lesson.publish
handle_log_info = cls_lesson.handle_log_info

class test_db__publish(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
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
                publish(self.fake_db, 1, 123)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = LessonModel(123, "CPU, RAM and ")
        
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_result = publish(self.fake_db, 1, 56)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db, 
                "UPDATE sow_lesson SET published = 1 WHERE id = 56;"
            , []
            )
            
            self.assertEqual(len(expected_result), len(actual_result))

