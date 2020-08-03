from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.schemesofwork.viewmodels import SchemeOfWorkGetAllViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model


class test_viewmodel_SchemeOfWorkGetAllViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = [Model(56)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self):
        
        # arrange
        
        data_to_return = [Model(56),Model(57),Model(58)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, auth_user=99)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))