from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, LessonDataAccess, handle_log_info

delete = Model.delete

class test_db__delete(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete(self.fake_db, 99, lesson_id=456)


    def test_should_call__delete(self):
         # arrange

        with patch.object(ExecHelper, 'delete', return_value=Model(102)):
            # act

            actual_result = delete(self.fake_db, 99, lesson_id=102)
            
            # assert
            ExecHelper.delete.assert_called()

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson__delete'
                , (102, 99)
                , handle_log_info)
            
            self.assertEqual(102, actual_result.id)