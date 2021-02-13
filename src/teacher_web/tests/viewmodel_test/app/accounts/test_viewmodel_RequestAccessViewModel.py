import json
from unittest import TestCase, skip
from django.http import Http404
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.teampermissions.viewmodels import TeamPermissionRequestAccessViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON 
from tests.test_helpers.mocks import fake_teacher_permission_model, fake_ctx_model

class test_viewmodel_RequestAccessViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_from_db=False))
    @patch.object(Model, "validate", return_value=True)
    def test_init_called_request_access__with_exception(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate):
        ''' request_access returns exception - SchemeOfWork must exist and User permission hasn't been granted '''
        # arrange        
        with patch.object(Model, "request_access", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(
                    db, 
                    request=mock_request, 
                    scheme_of_work_id=999, 
                    teacher_id=7089, 
                    teacher_name="Bill Gates",
                    permission="LESSON.NONE",
                    auth_user=fake_ctx_model()
                )
                
                self.viewmodel.execute()

                # assert functions were called
                SchemeOfWorkModel_get_model.assert_called()
                TeacherPermissionModel_get_model.assert_called()
                self.assertEqual(LESSON.NONE, self.viewmodel.permission)


    @patch.object(SchemeOfWorkModel, "get_model", return_value=None)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_from_db=False))
    @patch.object(Model, "validate", return_value=True)
    def test_init_raise_Http404__when_scheme_of_work_not_found(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate):
        ''' When the schemeofwork does not exist returns not found - SchemeOfWork must NOT exist and but ensure User permission hasn't been granted '''
        
        # arrange        

        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()

        self.mock_model = Mock()
        
        with self.assertRaises(Http404):
            # act
            self.viewmodel = ViewModel(
                db, 
                request=mock_request, 
                auth_user=99, 
                scheme_of_work_id=999, 
                teacher_id=78, 
                teacher_name="Suenos Blancos",
                permission = "LESSON.VIEWER"
            )
                
            self.viewmodel.execute()

            # assert functions were called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()
            TeacherPermissionModel_validate.assert_not_called()
            self.assertEqual(LESSON.VIEWER, self.viewmodel.permission)
            self.assertIsInstance(LESSON, self.viewmodel.permission)
        

    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    #Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True), is_authorised=True, is_from_db=True)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    @patch.object(Model, "validate", return_value=True)
    def test_init_raise_PermissionError__when_permission_already_granted(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate):
        ''' When the User permission does not exist returns not found - SchemeOfWork must NOT exist and but ensure User model does not exist '''
        
        # arrange
        
        data_to_return = None

        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()
        
        self.mock_model = Mock()

        mock_request = Mock()
        
        with patch.object(Model, "request_access", return_value=data_to_return):
            with self.assertRaises(PermissionError):
                # act
                self.viewmodel = ViewModel(
                    db, 
                    request=mock_request, 
                    auth_user=99, 
                    scheme_of_work_id=999, 
                    teacher_id=24, 
                    teacher_name="Pies Descalzos",
                    permission = "DEPARTMENT.STUDENT"
                )
                    
                self.viewmodel.execute()

                # assert functions were called
                SchemeOfWorkModel_get_model.assert_called()
                TeacherPermissionModel_get_model.assert_called()
                TeacherPermissionModel_validate.assert_called()
                Model.request_access.assert_not_called()
                self.assertEqual(DEPARTMENT.STUDENT, self.viewmodel.permission)


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    # Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(22, "A-Level Computing"), is_from_db=False)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_from_db=False))
    @patch.object(Model, "validate", return_value=True)
    def test_init_called_request_access__return_item(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate):
        ''' Grant permissions to user - SchemeOfWork must exist and User hasn't been granted permission '''
        
        # arrange
        #Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(99, name="La Sacre du Printemps Pt1: L'Adoration de las Terre"))
        data_to_return = TeacherPermissionModel_get_model
        data_to_return.published = 2

        with patch.object(Model, "request_access", return_value=data_to_return):
            db = Mock()
            db.cursor = MagicMock()

            mock_request = Mock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(
                    db=db,
                    request=mock_request,
                    scheme_of_work_id=101,
                    teacher_id=7039,
                    teacher_name="Igor Stravinsky",
                    permission = "DEPARTMENT.TEACHER",
                    auth_user=fake_ctx_model()
                )

            self.viewmodel.execute()
            
            # assert functions was called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()
            TeacherPermissionModel_validate.assert_called()
            Model.request_access.assert_called()
            self.assertEqual(DEPARTMENT.TEACHER, self.viewmodel.permission)
            self.assertEqual(TeacherPermissionModel_get_model.id, self.viewmodel.model.id)
