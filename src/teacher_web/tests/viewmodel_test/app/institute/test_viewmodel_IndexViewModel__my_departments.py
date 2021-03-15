from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.institute.viewmodels import InstituteIndexViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_institute import InstituteModel
from tests.test_helpers.mocks import *


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(InstituteModel, "get_my", return_value=[InstituteModel(56, "Lorem Ipsum")])
class test_viewmodel_IndexViewModel__my_departments(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()

            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(0, len(self.viewmodel.institutes[0].departments))


    def test_init_called_fetch__single_row(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        mock_institute = mock_auth_user.institute

        data_to_return = [Model(56, "Lorem Ipsum", institute=mock_institute)]
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()

            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(1, len(self.viewmodel.institutes[0].departments))
            self.assertEqual(0, len(self.viewmodel.institutes[0].departments[0].schemes_of_work))


    def test_init_called_fetch__multiple_rows(self, InstituteModel_get_my, mock_auth_user):
        
        # arrange
        
        mock_institute = mock_auth_user.institute

        data_to_return = [
            Model(57, "Lorem Ipsum", institute=mock_institute),
            Model(58, "Lorem Ipsum", institute=mock_institute),
            Model(59, "Lorem Ipsum", institute=mock_institute)
            ]
        
        with patch.object(Model, "get_my", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, top=5, auth_user=mock_auth_user)

            # assert functions was called
            InstituteModel_get_my.assert_called()
            Model.get_my.assert_called()
            
            self.assertEqual(1, len(self.viewmodel.institutes))
            self.assertEqual(3, len(self.viewmodel.institutes[0].departments))
