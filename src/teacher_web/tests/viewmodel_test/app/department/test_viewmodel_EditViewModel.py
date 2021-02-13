from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.department.viewmodels import DepartmentEditViewModel as ViewModel
from shared.models.cls_department import DepartmentModel as Model
from shared.models.cls_keyword import KeywordModel
from tests.test_helpers.mocks import *

@skip("not implemented")
@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    
    def test_execute_called_save__add_model_to_data(self, mock_auth_user):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tincidunt.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tincidunt.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(db=mock_db, request=mock_request, auth_user=mock_auth_user)
            
            # assert 

            self.assertEqual("", test_context.error_message)
            self.assertTrue(test_context.saved)
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.name)

    
    def test_execute_called_save__add_model_to_data__with_keywords(self, mock_auth_user):
        
        # arrange
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tinciduntx.",
                }


        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tinciduntx.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):


            return_keyword_model = KeywordModel(123, "RAM")
            return_keyword_model.is_valid = True

            # act

            mock_db = MagicMock()
            mock_db.cursor = MagicMock()

            test_context = ViewModel(db=mock_db, request=mock_request, auth_user=mock_auth_user)
            
            # assert 
            self.assertEqual("", test_context.error_message)
            self.assertEqual({}, test_context.model.validation_errors)

            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tinciduntx.", test_context.model.name)


    
    def test_execute_called_save__add_model_to_data__return_invalid(self, mock_auth_user):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"",
                }

        with patch.object(Model, "save", return_value=None):
                
            # act
            
            return_keyword_model = KeywordModel(4, term="Four")
            return_keyword_model.is_valid = True

            save_keyword.execute = Mock(return_value=return_keyword_model)
            save_keyword.model = return_keyword_model

            mock_db = MagicMock()
            mock_db.cursor = MagicMock()

            test_context = ViewModel(db=mock_db, request=mock_request, auth_user=mock_auth_user)

            # assert 

            self.assertEqual("", test_context.error_message)
            self.assertEqual("validation errors {'name': 'required'}", test_context.alert_message)
            self.assertFalse(test_context.saved)

            Model.save.assert_not_called()

            # return the invalid object
            self.assertEqual(99, test_context.model.id)
            self.assertEqual("", test_context.model.name)
            self.assertFalse(test_context.model.is_valid)
            self.assertEqual(1, len(test_context.model.validation_errors)) 
