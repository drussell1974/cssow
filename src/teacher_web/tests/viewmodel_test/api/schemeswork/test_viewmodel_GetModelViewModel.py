from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.schemesofwork.viewmodels import SchemeOfWorkGetModelViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model


class test_viewmodel_GetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self):
        
        # arrange        
        with patch.object(Model, "get_model", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, 99, auth_user=99)


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 123, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(67, name="Integer ac ante")
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, 456, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(67, self.viewmodel.model["id"])
            self.assertEqual("Integer ac ante", self.viewmodel.model["name"])


