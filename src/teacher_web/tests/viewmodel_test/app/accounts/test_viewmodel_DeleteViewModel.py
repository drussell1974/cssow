import json
from unittest import TestCase, skip
from django.http import Http404
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.teampermissions.viewmodels import TeamPermissionDeleteViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from tests.test_helpers.mocks import fake_teacher_permission_model

class test_viewmodel_DeleteViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    def test_init_called_delete__with_exception(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange        
        with patch.object(Model, "delete", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, auth_user=99, scheme_of_work_id=999, teacher_id=78)
                self.viewmodel.execute()

                # assert functions were called
                SchemeOfWorkModel_get_model.assert_called()
                TeacherPermissionModel_get_model.assert_called()



    @patch.object(SchemeOfWorkModel, "get_model", return_value=None)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    def test_init_raise_Http404__when_scheme_of_work_not_found(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange        

        db = MagicMock()
        db.cursor = MagicMock()

        self.mock_model = Mock()
        
        with self.assertRaises(Http404):
            # act
            self.viewmodel = ViewModel(db, auth_user=99, scheme_of_work_id=999, teacher_id=78)
            self.viewmodel.execute()

            # assert functions were called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()
        

    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model(is_from_db=False))
    def test_init_raise_Http404__when_permission_model_not_found(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
    
        db = MagicMock()
        db.cursor = MagicMock()

        self.mock_model = Mock()
        
        with self.assertRaises(Http404):
            # act
            self.viewmodel = ViewModel(db, auth_user=99, scheme_of_work_id=999, teacher_id=78)
            self.viewmodel.execute()

            # assert functions were called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    # Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(22, "A-Level Computing"), is_from_db=True)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    def test_init_called_delete__no_return_rows(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=101, teacher_id=2069, auth_user=99)
            self.viewmodel.execute()
            
            # assert functions was called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()
            Model.delete.assert_called()


    @patch.object(SchemeOfWorkModel, "get_model", return_value=SchemeOfWorkModel(22, "A-Level Computing", is_from_db=True))
    # Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(22, "A-Level Computing"), is_from_db=True)
    @patch.object(Model, "get_model", return_value=fake_teacher_permission_model())
    def test_init_called_delete__return_item(self, SchemeOfWorkModel_get_model, TeacherPermissionModel_get_model):
        
        # arrange
        # Model(TeacherModel(24, "Jane Doe", DepartmentModel(15, "Computer Science")), SchemeOfWorkModel(99, name="La Sacre du Printemps Pt1: L'Adoration de las Terre"))
        
        data_to_return = TeacherPermissionModel_get_model
        data_to_return.published = 2

        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, scheme_of_work_id=101, teacher_id=7039, auth_user=99)
            self.viewmodel.execute()
            
            # assert functions was called
            SchemeOfWorkModel_get_model.assert_called()
            TeacherPermissionModel_get_model.assert_called()
            Model.delete.assert_called()
            self.assertEqual(TeacherPermissionModel_get_model.id, self.viewmodel.model.id)
