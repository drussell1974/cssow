from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log import handle_log_info
from shared.models.cls_lesson import LessonDataAccess, LessonModel, handle_log_info

publish = LessonDataAccess.publish


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

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                publish(self.fake_db, 1, 123, 99)


    def test_should_call_execCRUDSql(self):
         # arrange
        model = LessonModel(123, "CPU, RAM and ")
        
        expected_result = []

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = publish(self.fake_db, 56, 99)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db, 
               'lesson__publish'
               , (56, 1, 99)
               , []
            )
            
            self.assertEqual(len(expected_result), len(actual_result))

