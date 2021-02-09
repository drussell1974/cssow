from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_resource import ResourceModel as Model, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__delete(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
    def tearDown(self):
        pass

    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.delete(self.fake_db, model.id, mock_auth_user)


    def test_should_call__delete(self, mock_auth_user):
         # arrange
        model = Model(1, title="How to make more unit tests", publisher="Unit test",  lesson_id=15, scheme_of_work_id=115)

        expected_result = [(1)]

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(self.fake_db, model.id, mock_auth_user)
            
            # assert

            ExecHelper.delete.assert_called_with(self.fake_db, 
                'lesson_resource__delete'
                , (1, mock_auth_user.id)
                , handle_log_info)

            self.assertEqual(1, actual_result[0])