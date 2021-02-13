import json
from unittest import TestCase, skip
from django.http import Http404
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.teampermissions.viewmodels import TeamPermissionRequestLoginViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model, DepartmentModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON 
from tests.test_helpers.mocks import fake_teacher_permission_model, fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_RequestLoginViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    @patch.object(Model, "validate", return_value=True)
    def test_init_raise_exception_when_missing__scheme_of_work_id(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate, mock_ctx_model):
        
        # arrange     
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock()
        
        mock_get_context_data = MagicMock(return_value={})
        

        with self.assertRaises(KeyError):
            # act
            self.viewmodel = ViewModel(
                db, 
                request=mock_request, 
                get_context_data = mock_get_context_data,
                auth_user=101,
                permission=DEPARTMENT.TEACHER
            )
            
            self.viewmodel.view()

            # assert

            self.assertTrue(self.viewmodel.request_made)
            self.assertEqual(11, self.viewmodel.scheme_of_work_id)

            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_authorised=False))
    @patch.object(Model, "validate", return_value=True)
    def test_init_when_permssion_requested__return_true(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate, mock_ctx_model):
        
        # arrange
        
        #data_to_return = Model( TeacherModel(24, name="Jane Doe", department=DepartmentModel(15, name="Computer Science", institute=InstituteModel(12776111277611, "Lorem Ipsum"))), scheme_of_work=SchemeOfWorkModel(99, name="La Sacre du Printemps Pt1: L'Adoration de las Terre"))
        data_to_return = TeacherPermissionModel_get_model
        data_to_return.published = 2

        db = Mock()
        db.cursor = MagicMock()

        mock_request = Mock()

        self.mock_model = Mock()

        fake_kwargs = {'scheme_of_work_id': 11, 'permission': DEPARTMENT.TEACHER}
        
        # act

        mock_get_context_data = MagicMock(return_value=fake_kwargs)

        self.viewmodel = ViewModel(
            db, 
            request=mock_request, 
            get_context_data = mock_get_context_data,
            auth_user=mock_ctx_model,
            scheme_of_work_id=11,
            permission=DEPARTMENT.TEACHER
        )

        result = self.viewmodel.view()

        # assert

        self.assertTrue(self.viewmodel.request_made)
        self.assertEqual(11, self.viewmodel.scheme_of_work_id)
        self.assertEqual(fake_kwargs, result)
 
        SchemeOfWorkModel_get_model.assert_called()
        TeacherPermissionModel_get_model.assert_called()
        TeacherPermissionModel_validate.assert_called()
        mock_get_context_data.assert_called()



    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    @patch.object(Model, "validate", return_value=True)
    def test_init_when_permssion_requested__return_false(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model, TeacherPermissionModel_validate, mock_ctx_model):
        
        # arrange
        
        #data_to_return = Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(99, name="La Sacre du Printemps Pt1: L'Adoration de las Terre"))
        data_to_return = TeacherPermissionModel_get_model
        data_to_return.published = 2

        db = Mock()
        db.cursor = MagicMock()

        mock_request = Mock()

        self.mock_model = Mock()

        fake_kwargs = {'scheme_of_work_id': 11, 'permission': DEPARTMENT.TEACHER}
        
        # act

        mock_get_context_data = MagicMock(return_value=fake_kwargs)

        self.viewmodel = ViewModel(
            db, 
            request=mock_request, 
            get_context_data = mock_get_context_data,
            auth_user=mock_ctx_model,
            scheme_of_work_id=11,
            permission=DEPARTMENT.TEACHER
        )

        result = self.viewmodel.view()

        # assert

        self.assertFalse(self.viewmodel.request_made)
        self.assertEqual(11, self.viewmodel.scheme_of_work_id)
        self.assertEqual(fake_kwargs, result)
        
        SchemeOfWorkModel_get_model.assert_called()
        TeacherPermissionModel_get_model.assert_called()
        TeacherPermissionModel_validate.assert_called()
        mock_get_context_data.assert_called()
