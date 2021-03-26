from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.default.viewmodels import DefaultIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(DepartmentModel, "get_my", return_value = [DepartmentModel(76, name="Lorum Ipsum", institute=InstituteModel(127671276711, "Lorem Ipsum"), is_from_db=True)])
@patch.object(InstituteModel, "get_my", return_value=[InstituteModel(127671276711, "Lorem Ipsum", is_from_db=True)])
class test_viewmodel_IndexViewModel__my_schemes_of_work(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, InstituteModel_get_my, DepartmentModel_get_my, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_my.assert_called()
            self.assertEqual(0, len(self.viewmodel.schemes_of_work))


    def test_init_called_fetch__single_row(self, InstituteModel_get_my, DepartmentModel_get_my, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(56, name="Lorem", study_duration=2, start_study_in_year=10)]

        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)
            
            # assert functions was called
            Model.get_my.assert_called()
            self.assertEqual(1, len(self.viewmodel.departments[0].schemes_of_work))


    def test_init_called_fetch__multiple_rows(self, InstituteModel_get_my, DepartmentModel_get_my, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(56, name="Lorem1", study_duration=2, start_study_in_year=10),Model(57, name="Lorem2", study_duration=2, start_study_in_year=10),Model(58, name="Lorem3", study_duration=2, start_study_in_year=10)]
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_my.assert_called()
            self.assertEqual(3, len(self.viewmodel.departments[0].schemes_of_work))
