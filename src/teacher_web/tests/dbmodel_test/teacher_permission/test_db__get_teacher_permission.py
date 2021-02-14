from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, handle_log_info
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_teacher_permission_model, fake_ctx_model

#@patch("shared.models.cls_teacher_permission.TeacherPermissionModel", return_value=fake_teacher_permission_model())
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_teacher_permission(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(KeyError):
                Model.get_model(self.fake_db, SchemeOfWorkModel(99, name="Computer Sciemce", department_id=45, institute_id=74), auth_user=mock_auth_user)

    
    def test__should_call__select__return_no_permissions(self, mock_auth_user):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.NONE), int(LESSON.NONE), int(DEPARTMENT.NONE), "James Joyce", False)]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            model = Model.get_model(self.fake_db, SchemeOfWorkModel(99, name="Ulysses", department_id=45, institute_id=74), auth_user=mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (99, mock_auth_user.auth_user_id, mock_auth_user.department_id, mock_auth_user.institute_id, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(99, model.scheme_of_work_id)
            #self.assertEqual("Ulysses", model.scheme_of_work_name)
            self.assertEqual(SCHEMEOFWORK.NONE, int(model.scheme_of_work_permission))
            self.assertEqual(LESSON.NONE, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            self.assertFalse(model.is_authorised)
            

    def test__should_call__select__return_has_permission_to_view(self, mock_auth_user):
        # arrange
        expected_result = [(int(SCHEMEOFWORK.EDITOR), int(LESSON.VIEWER), int(DEPARTMENT.NONE), "Frank Herbert", True)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            
            # act
            
            model = Model.get_model(self.fake_db, SchemeOfWorkModel(14, name="Dune", department_id=45, institute_id=74), auth_user=mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_teacher_permissions"
                , (14, mock_auth_user.auth_user_id, mock_auth_user.department_id, mock_auth_user.institute_id, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            
            self.assertEqual(14, model.scheme_of_work_id)
            #self.assertEqual("Dune", model.scheme_of_work.name)
            self.assertEqual(SCHEMEOFWORK.EDITOR, model.scheme_of_work_permission)
            self.assertEqual(LESSON.VIEWER, model.lesson_permission)
            self.assertEqual(DEPARTMENT.NONE, model.department_permission)
            self.assertTrue(model.is_authorised)
