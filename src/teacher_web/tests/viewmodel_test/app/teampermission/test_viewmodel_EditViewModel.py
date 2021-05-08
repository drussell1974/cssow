from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.teampermissions.viewmodels import TeamPermissionEditViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass

    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work(id=22))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    def test_execute_should_call_save__when_model_is_valid(self, mock_auth_user, mock_bc, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = { 
            "scheme_of_work_id": 22,
            "teacher_id":24,
            "department_permission": int(DEPARTMENT.TEACHER),
            "scheme_of_work_permission": int(SCHEMEOFWORK.VIEWER),
            "lesson_permission": int(LESSON.VIEWER), 
            "join_code":"ABCDEFGH",
            "published":"PUBLISH",
        }
    
        with patch.object(Model, "save", return_value = TeacherPermissionModel_get_model):

            # act

            test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=22, teacher_id=6049, auth_user=mock_auth_user)
            test_context.execute()

            # assert

            Model.save.assert_called()
            SchemeOfWorkModel_get_model.assert_called()

            # return the valid object

            self.assertEqual({}, test_context.model.validation_errors)
            self.assertTrue(test_context.model.is_valid)
            self.assertEqual(22, test_context.scheme_of_work.id)
            

    @patch.object(SchemeOfWorkModel, "get_model", return_value=mock_scheme_of_work())
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_authorised=False))
    def test_execute_should_not_call_save__when_return_invalid(self, mock_auth_user, mock_bc, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange
        
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = { 
            "scheme_of_work_id": 22,
            "teacher_id": 99,
            "teacher_name": "Proin Massa",
            "department_id": 87,
            "department_permission": int(DEPARTMENT.ADMIN) + 1,
            "scheme_of_work_permission": int(SCHEMEOFWORK.EDITOR),
            "lesson_permission": int(LESSON.EDITOR),
            "published":"PUBLISH",
        }
        with patch.object(Model, "save", return_value=None):
            
            # act
            
            test_context = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=22, teacher_id=6059, auth_user=mock_auth_user)
            test_context.execute()
            
            # assert
            
            Model.save.assert_not_called()
            
            SchemeOfWorkModel_get_model.assert_called()
