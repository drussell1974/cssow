from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.institutes.viewmodels import InstituteGetAllViewModel as ViewModel
from shared.models.core.context import Ctx
from shared.models.cls_institute import InstituteModel as Model
from tests.test_helpers.mocks import fake_ctx_model


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_InstituteGetAllViewModel(TestCase):

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
            self.viewmodel = ViewModel(db, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, "Lorem Ipsum")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, "Tic"),Model(57, "Tac"),Model(58, "Toe")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))