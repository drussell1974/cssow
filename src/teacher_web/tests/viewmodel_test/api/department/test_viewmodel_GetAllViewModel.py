from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.departments.viewmodels import DepartmentGetAllViewModel as ViewModel
from shared.models.core.context import Ctx
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_institute import InstituteModel
from tests.test_helpers.mocks import fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_DepartmentGetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 1276711, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, "Ipsum", institute=InstituteModel(1276711, "Lorum"))]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 1276711, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [
            Model(56, "Tic", institute=InstituteModel(1276711, "Lorum")),
            Model(57, "Tac", institute=InstituteModel(1276711, "Lorum")),
            Model(58, "Toe", institute=InstituteModel(1276711, "Lorum"))]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 1276711, auth_user=fake_ctx_model())

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))