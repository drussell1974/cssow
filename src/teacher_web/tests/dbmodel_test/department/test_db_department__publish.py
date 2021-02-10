from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
#from shared.models.cls_institute import InstituteModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__publish_by_id(TestCase):


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

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                DepartmentModel.publish_by_id(self.fake_db, 1, 123)


    def test_should_call_update(self, mock_auth_user):
        # arrange
        
        expected_result = [(123,)]

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = DepartmentModel.publish_by_id(self.fake_db, 123, mock_auth_user)
            
            # assert
            ExecHelper.update.assert_called_with(self.fake_db,
                "department__publish"
                , (123, 1, mock_auth_user.id)
                , handle_log_info)
            
            self.assertEqual(1, len(actual_result))

