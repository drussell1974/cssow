from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel as Model, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__delete_unpublished(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.delete_unpublished(self.fake_db, 1, auth_user=99)


    def test_should_call_delete(self, mock_auth_user):
         # arrange
        model = Model(12, "")
        
        expected_result = 5

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete_unpublished(self.fake_db, 12, auth_user=mock_auth_user)
            
            # assert
            ExecHelper.delete.assert_called()

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson__delete_unpublished'
                , (12, mock_auth_user.id)
                , handle_log_info)

            self.assertEqual(expected_result, actual_result)
