from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, handle_log_info

# Test Context

delete_unpublished = Model.delete_unpublished


class test_db__delete_unpublished(TestCase):


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

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call_delete(self):
         # arrange
        model = Model(12, "")
        
        expected_result = 5

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = delete_unpublished(self.fake_db, 12, auth_user=99)
            
            # assert
            ExecHelper.delete.assert_called()

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson__delete_unpublished'
                , (12, 99)
                , handle_log_info)

            self.assertEqual(expected_result, actual_result)
