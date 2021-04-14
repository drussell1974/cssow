from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.academic_years.viewmodels import AcademicYearEditViewModel as ViewModel
from shared.models.cls_academic_year import AcademicYearModel as Model
from shared.models.cls_keyword import KeywordModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass

    
    def test_execute_called_save__new_academic_get(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        with patch.object(Model, "get_model", return_value=Model(2020, "2020-09-04", "2021-07-18", True)):
        
            # act

            test_context = ViewModel(db=mock_db, request=mock_request, year=2020, auth_user=mock_auth_user)
            
            # assert 

            self.assertEqual("", test_context.error_message)
            self.assertFalse(test_context.saved)
            
            self.assertEqual(2020, test_context.model.id)
            self.assertEqual(datetime(2020, 9, 4, 0, 0), test_context.model.start_date)
            self.assertEqual(datetime(2021, 7, 18, 0, 0), test_context.model.end_date)
            # TODO: #458 reinstate
            #self.assertTrue(test_context.model.is_valid)
            self.assertEqual({}, test_context.model.validation_errors) 


    def test_execute_called_save__existing_academic_year(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "start_date":"2020-09-04",
                    "end_date": "2021-07-18",
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        on_save__data_to_return = Model(2020, "2020-09-04", "2021-07-18", True)
        with patch.object(Model, "get_model", return_value=Model(2020, "2020-09-01", "2021-07-15", False)):
            with patch.object(Model, "save", return_value=on_save__data_to_return):

                # act

                test_context = ViewModel(db=mock_db, request=mock_request, year=2020, auth_user=mock_auth_user)
                
                test_context.execute()

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertTrue(test_context.saved)
                
                Model.save.assert_called()

                self.assertEqual(2020, test_context.model.id)
                self.assertEqual(datetime(2020, 9, 4, 0, 0), test_context.model.start_date)
                self.assertEqual(datetime(2021, 7, 18, 0, 0), test_context.model.end_date)
                # TODO: #458 reinstate
                #self.assertTrue(test_context.model.is_valid)
                self.assertEqual({}, test_context.model.validation_errors) 

    
    def test_execute_called_save__add_model_to_data__return_invalid(self, mock_auth_user):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "start_date": "2020-09-01",
                    "end_date": "2100-07-15", # invalid date
                }

        with patch.object(Model, "get_model", return_value=Model(2020, "2020-09-01", "2021-07-15", False)):
            with patch.object(Model, "save", return_value=None):
                    
                # act

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, year=2020, auth_user=mock_auth_user)
                
                test_context.execute()

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'end_date': '2100-07-15 00:00:00 should be between 1700-01-01 00:00:00 and 2099-12-31 00:00:00'}", test_context.alert_message)
                self.assertFalse(test_context.saved)
                
                Model.get_model.assert_called()

                Model.save.assert_not_called()

                # return the invalid object
                self.assertEqual(2020, test_context.model.id)
                self.assertEqual(datetime(2020, 9, 1, 0, 0), test_context.model.start_date)
                self.assertEqual(datetime(2100, 7, 15, 0, 0), test_context.model.end_date)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
