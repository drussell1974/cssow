from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.resources.viewmodels import ResourceGetModelViewModel as ViewModel
from shared.models.cls_resource import ResourceModel as Model


class test_viewmodel_GetModelViewModel(TestCase):

    def setUp(self):        
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_model", return_value=data_to_return):

            # act
            self.viewmodel = ViewModel(self.fake_db, 99, 12, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = Model(34, title="How to save the world in a day")
        

        with patch.object(Model, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(self.fake_db, 34, scheme_of_work_id=109, auth_user=99)

            # assert functions was called
            Model.get_model.assert_called()

            self.assertEqual(34, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.title)