from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, TeacherPermissionDataAccess as DataAccess, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "John Doe", department=DepartmentModel(67, "Computer Science")))
@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(9999, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__delete(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_user_model, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        scheme_of_work = MagicMock(id=99, name="A-Level Computer Science")

        model = Model(mock_user_model, scheme_of_work)

        with patch.object(ExecHelper, 'delete', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                Model.delete(self.fake_db, model, 99)


    def test_should_call__delete__when__is_new__is_false__and__published_is_2(self, mock_user_model, mock_auth_user):
        # arrange

        scheme_of_work = MagicMock(id=19, name="A-Level Computer Science")

        model = Model(mock_user_model, scheme_of_work, SCHEMEOFWORK.VIEWER, SCHEMEOFWORK.EDITOR, DEPARTMENT.TEACHER)
        model.created = '2021-01-24 07:18:18.677084'
        model.is_new = Mock(return_value=False)
        model.published = 2

        # mock functions not being tested

        expected_result = (19,79)

        with patch.object(ExecHelper, 'delete', return_value=expected_result):
            # act

            actual_result = Model.delete(self.fake_db, model, auth_user=mock_auth_user)
            
            # assert

            ExecHelper.delete.assert_called_with(
                self.fake_db, 
                'scheme_of_work__has__teacher_permission__delete'
                , (19, mock_user_model.id, mock_auth_user.id)
                , handle_log_info)
