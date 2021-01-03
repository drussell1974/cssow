import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from django.http import Http404


# test context
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from shared.models.cls_registereduser import RegisteredUserModel as Model
#from django.contrib.auth import login, authenticate
from app.accounts.viewmodels import AccountsRegisterViewModel as ViewModel, RegisterUserForm


@skip("TODO: 206 inherit RegisteredUserForm from UserCreationForm -accounts/login.RegisterUserModel may not be required")
class test_viewmodel_AccountsRegisterViewModel(ViewModelTestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_init_on_GET__edit_new_model(self):
        
        # arrange

        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )

        # TODO: Mock Instance

        mock_model = Model()

        # act
        with patch.object(RegisterUserForm, 'is_valid', return_value=True):
            viewmodel = ViewModel(self.mock_db, mock_request)
            
            # assert 

            # assert functions was to return data called

            self.assertViewModelContent(viewmodel
                , ""
                , "Account"
                , "Registration"
                , {}
            )
        
        
    def test_init_on_POST_valid(self):
        
        # arrange
        model = Model()
        model.is_valid = True

        with patch.object(Model, "save"):
            # act
            mock_post = Mock(
                POST = {"username":"Loremipsum", "password1":"password" },
                method = "POST"
            )
            
            test_context = ViewModel(self.mock_db, mock_post)

            # assert 
        
            # data has been saved
                            
            # assert functions was called
            Model.save.assert_called()

            #ui_view = viewmodel.view().content

            #self.assertEqual({'user': '', 'password1': ''}, ui_view["content"]["active_model"])
            #self.assertEqual({'letter_prefix': 'aB is not valid. value must be an uppercase letter'}, ui_view["content"]["validation_errors"])



    def test_init_on_POST__invalid(self):
        
        # arrange
        model = Model()
        model.is_valid = False

        with patch.object(Model, "is_valid", returns_value=False):
            with patch.object(Model, "save"):

                # act (invalid data)
                mock_post = Mock(
                    POST = {"username":"", "password1":"", "email": "" },
                    method = "POST"
                )

                #"", "Vivamus venenatis interdum sem.", "Quisque imperdiet lectus efficitur enim porttitor, vel iaculis ligula ullamcorper"

                viewmodel = ViewModel(self.mock_db, mock_post)
                
                # assert 
            
                # assert functions was called
                Model.save.assert_not_called()
        
                # return invalid model with validation
                
                self.assertViewModelContent(viewmodel
                    , ""
                    , "Account"
                    , "Registration"
                    , {}
                )

                #ui_view = viewmodel.view().content

                #self.assertEqual({'display_name': '', 'id': 0, 'published_state': 'unknown-state'}, ui_view["content"]["active_model"])
                #self.assertFalse(ui_view["content"]["data"]["model"].is_valid)
                #self.assertEqual({'letter_prefix': 'aB is not valid. value must be an uppercase letter'}, ui_view["content"]["validation_errors"])
