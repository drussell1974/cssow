from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.notifications.viewmodels import NotificationDeleteViewModel as ViewModel
from tests.test_helpers.mocks import fake_ctx_model
from shared.models.cls_notification import NotifyModel as Model
from shared.models.core.log_type import LOG_TYPE


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_NotificationDeleteViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__not_exists(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, event_log_id=101, auth_user=mock_ctx_model)

            # assert
            Model.delete.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))

    
    def test_init_called_delete__existing_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [232734343]

        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, event_log_id=232734343, auth_user=mock_ctx_model)

            # assert
            Model.delete.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))
