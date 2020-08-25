import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.eventlogs.viewmodels import EventLogDeleteOldViewModel as ViewModel
from shared.models.cls_eventlog import EventLogModel as Model


class fake_settings:
    MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS = 7
    
class test_viewmodel_DeleteOldViewModel(TestCase):


    def setUp(self):    
        self.fake_settings = fake_settings()

        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exceptioin__should_show_error_message(self):
        
        # arrange        
        with patch.object(Model, "delete", side_effect=KeyError("There was an error executing the stored procedure")):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "days": 30 }

            self.mock_model = Mock()

            #with self.assertRaises(KeyError):
                # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            self.assertEqual("'There was an error executing the stored procedure'", self.viewmodel.error_message)


    def test_init_called_delete__should_not_call_delete_when_GET_request(self):
        
        # arrange        
        with patch.object(Model, "delete"):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "GET"
            mock_request.POST = { "days": 30 }

            # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            # assert
            Model.delete.assert_not_called()


    def test_init_called_delete__should_not_call_delete_when_days_less_than_7(self):
        
        # arrange        
        with patch.object(Model, "delete"):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "days": 6 }
            
            
            #with self.assertRaises(Exception):
                # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            # assert
            Model.delete.assert_not_called()


    def test_init_called_delete__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "days": 7 }

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            # assert functions was called
            Model.delete.assert_called_with(db, 7, 6079)

            self.assertEqual([], self.viewmodel.model)


    def test_init_called_delete__return_item(self):
        
        # arrange
        
        with patch.object(Model, "delete", return_value=1):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "days": 14, "page": 1, "pagesize":20 }
            
            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            # assert functions was called
            Model.delete.assert_called_with(db, 14, 6079)
            self.assertEqual("1 event logs deleted", self.viewmodel.alert_message)
            self.assertEqual([], self.viewmodel.model)


    def test_init_called_delete__return_items(self):
        
        # arrange
        
        with patch.object(Model, "delete", return_value=3):

            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()
            mock_request.method = "POST"
            mock_request.POST = { "days": 28 }

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db, mock_request, self.fake_settings, auth_user=6079)

            # assert functions was called
            Model.delete.assert_called_with(db, 28, 6079)
            self.assertEqual("3 event logs deleted", self.viewmodel.alert_message)
            self.assertEqual([], self.viewmodel.model)
