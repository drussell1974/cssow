from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.resources.viewmodels import ResourceGetModelViewModel as ViewModel
from shared.models.cls_resource import ResourceModel as Model


class test_viewmodel_ResourceGetModelViewModel(TestCase):

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
                self.viewmodel = ViewModel(db, resource_id=999, scheme_of_work_id=90, auth_user=99)


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, resource_id=123, scheme_of_work_id=90, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(456, title="Cras eleifend pulvinar lacinia.")
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, resource_id=456, scheme_of_work_id=90, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(456, self.viewmodel.model["id"])
            self.assertEqual("Cras eleifend pulvinar lacinia.", self.viewmodel.model["title"])