from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from api.notifications.viewmodels import NotificationIndexViewModel as ViewModel
from tests.test_helpers.mocks import fake_ctx_model
from shared.models.cls_notification import NotifyModel as Model
from shared.models.core.log_type import LOG_TYPE

class fake_settings:
    MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS = 7
    PAGER = { 
        "default": {
             "page": 2, "pagesize": 10, "pagesize_options": [5,10,25,50,100]
        },
        "notifications": {
             "page": 1, "pagesize": 100, "pagesize_options": [100,]
        }
    }

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_NotificationIndexViewModel(TestCase):

    def setUp(self):
        self.fake_settings = fake_settings       
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_notifications", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, settings=fake_settings, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_notifications.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))

    
    def test_init_called_fetch__single_row(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [Model(56, 
            notify_message="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.",
            reminder="2021-04-05T07:46",
            event_type=LOG_TYPE.Warning,
            action="http://localhost/dosomething/2"
        )]

        with patch.object(Model, "get_notifications", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, settings=fake_settings, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_notifications.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self, mock_ctx_model):
        
        # arrange
        
        data_to_return = [
            Model(56, 
                notify_message="Lorem ipsum dolor sit amet",
                message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce nec elit quis lorem semper rutrum quis sed turpis.",
                reminder="2021-04-05T07:46",
                event_type=LOG_TYPE.Warning,
                action="http://localhost/dosomething/1"
            ),
            Model(57, 
                notify_message="Suspendisse semper neque diam.",
                message="Suspendisse semper neque diam, posuere facilisis quam vulputate eu. In et lorem mi.",
                reminder="2021-04-05T07:46",
                event_type=LOG_TYPE.Information,
                action="http://localhost/dosomething/2"
            ),
            Model(58, 
                notify_message="Donec lacinia diam vel euismod aliquam.",
                message="Nulla vulputate nisi at ipsum porttitor, sit amet sagittis ipsum convallis. Donec lacinia diam vel euismod aliquam.",
                reminder="2021-04-05T07:46",
                event_type=LOG_TYPE.Error,
                action="http://localhost/dosomething/3"
            )
        ]
        
        with patch.object(Model, "get_notifications", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, settings=fake_settings, auth_user=mock_ctx_model)

            # assert functions was called
            Model.get_notifications.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))
