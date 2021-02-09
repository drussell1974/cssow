from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_resource import ResourceModel as Model, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__publish_item(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, "")

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.publish_item(self.fake_db, 999, 99)


    def test_should_call__update(self, mock_auth_user):
         # arrange
        model = Model(123, "CPU, RAM and ")
        model.lesson_id = 101
        
        expected_result = []

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = Model.publish_item(self.fake_db, model.id, 78, mock_auth_user)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db, 
            'lesson_resource__publish_item'
            , (123, 78, 1, mock_auth_user.id)
            )
            
            self.assertEqual(len(expected_result), len(actual_result))

