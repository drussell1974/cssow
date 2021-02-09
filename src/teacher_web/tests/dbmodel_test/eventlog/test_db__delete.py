from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_eventlog import EventLogModel as Model, EventLogDataAccess, handle_log_info
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

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                delete(self.fake_db, 0, 99)


    def test_should_call__delete(self, mock_auth_user):
        # arrange
        
        expected_result = 2001

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(db=self.fake_db, scheme_of_work_id=69, older_than_n_days=31, auth_user=mock_auth_user)

            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                "logging__delete"
                , (69, 31, mock_auth_user.id)
                , handle_log_info)

            # check subsequent functions where called

            self.assertEqual(2001, actual_result)
           