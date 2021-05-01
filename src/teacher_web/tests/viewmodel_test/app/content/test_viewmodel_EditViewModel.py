import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from django.http import Http404
from tests.viewmodel_test.viewmodel_testcase import ViewModelTestCase
from app.content.viewmodels import ContentEditViewModel as ViewModel
from shared.models.cls_content import ContentModel as Model
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_EditViewModel(ViewModelTestCase):

    def setUp(self):
        self.mock_db = MagicMock()
        self.mock_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_init_called_on_GET__raises_404_if_scheme_of_work_not_found(self, mock_auth_user, mock_bc):
        
        # arrange

        SchemeOfWorkModel.get_model = Mock(return_value=None)

        db = MagicMock()
        db.cursor = MagicMock()
        mock_model = Model(12, "", "")

        mock_post = Mock(
            method = "GET"
        )

        with self.assertRaises(Http404):
            # act
            ViewModel(db=self.mock_db, request=mock_post, scheme_of_work_id=234, content_id=67, auth_user=mock_auth_user)

            # assert functions was to return data called
            SchemeOfWorkModel.get_model.assert_called()


    def test_init_on_POST__raises_404_if_scheme_of_work_not_found(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=None)

        db = MagicMock()
        db.cursor = MagicMock()

        mock_post = Mock(
            method = "POST"
        )
        
        with self.assertRaises(Http404):
            # act
            ViewModel(db=self.mock_db, request=mock_post, scheme_of_work_id=234, content_id=67, auth_user=mock_auth_user)

            # assert functions was to return data called
            SchemeOfWorkModel.get_model.assert_called()


    def test_init_on_GET__edit_new_model(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=SchemeOfWorkModel(23, name="Vivamus venenatis interdum sem.", study_duration=3, start_study_in_year=7, is_from_db=True))


        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )

        # act
        viewmodel = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=234, content_id=0, auth_user=mock_auth_user)
        
        # assert 

        # assert functions was to return data called
        SchemeOfWorkModel.get_model.assert_called()

        self.assertViewModelContent(mock_request, viewmodel
            , ""
            , "Vivamus venenatis interdum sem."
            , "Create new content for Vivamus venenatis interdum sem."
            , {}
        )


    def test_init_on_GET__edit_existing_model(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=SchemeOfWorkModel(23, name="Vivamus venenatis interdum sem.", study_duration=2, start_study_in_year=10, is_from_db=True))
        Model.get_model = Mock(return_value=Model(101,"dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti", "Z", is_from_db=True))    
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )

        # act
        viewmodel = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=234, content_id=101, auth_user=mock_auth_user)
        
        # assert 
        
        # assert functions was to return data called
        Model.get_model.assert_called()

        self.assertViewModelContent(mock_request, viewmodel
            , ""
            , "Vivamus venenatis interdum sem."
            , "Edit: dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti"
            , {}
        )


    def test_init_on_GET__edit_existing_model__raise_404_if__content_model__not_found(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=SchemeOfWorkModel(23, name="Vivamus venenatis interdum sem.", study_duration=3, start_study_in_year=7, is_from_db=True))
        
        Model.get_model = Mock(return_value=None)    
        
        db = MagicMock()
        db.cursor = MagicMock()

        mock_request = Mock(
            method = "GET"
        )

        
        # call view
        with self.assertRaises(Http404):
            # act
            viewmodel = ViewModel(db=self.mock_db, request=mock_request, scheme_of_work_id=234, content_id=67, auth_user=mock_auth_user)
        
            # assert 
            
            # assert functions was to return data called
            SchemeOfWorkModel.get_model.assert_called()

            viewmodel.view()
            

    def test_init_on_POST_valid_model__is_content_ready__true__and__save(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=mock_scheme_of_work(id=32))

        on_save__data_to_return = Model(92, "Quisque eu venenatis sem", "A")
        on_save__data_to_return.is_valid = True

        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act
            mock_post = Mock(
                POST = {"id":"0", "description":"Proin id massa metus. Aliqua tincidunt.", "letter_prefix":"B","key_stage_id":"4","published":"PUBLISH"},
                method = "POST"
            )
            
            test_context = ViewModel(db=self.mock_db, request=mock_post, scheme_of_work_id=234, content_id = 703, auth_user=mock_auth_user)
                                        
            # assert 
        
            # data has been saved
                            
            self.assertTrue(test_context.is_content_ready)

            # assert functions was called
            Model.save.assert_called()

            
    def test_init_on_POST__invalid_model_is_content_ready__false(self, mock_auth_user, mock_bc):
        
        # arrange
        SchemeOfWorkModel.get_model = Mock(return_value=SchemeOfWorkModel(23, name="Vivamus venenatis interdum sem.", study_duration=3, start_study_in_year=7, is_from_db=True))

        on_save__data_to_return = Model(92, "Quisque eu venenatis sem", "aaa")
                
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act
            mock_post = Mock(
                POST = {"id":"12","description":"Vivamus venenatis interdum sem.", "letter_prefix":"aB", "key_stage_id":"4", "published":"PUBLISH"},
                method = "POST"
            )

            #"", "Vivamus venenatis interdum sem.", "Quisque imperdiet lectus efficitur enim porttitor, vel iaculis ligula ullamcorper"

            viewmodel = ViewModel(db=self.mock_db, request=mock_post, scheme_of_work_id=234, content_id=67, auth_user=mock_auth_user)
            
            # assert 
        
            # data has NOT been saved
                            
            self.assertFalse(viewmodel.is_content_ready)

            # assert functions was called
            Model.save.assert_not_called()
    
            self.assertViewModelContent(mock_post, viewmodel
                , ""
                , "Vivamus venenatis interdum sem."
                , "Edit: Vivamus venenatis interdum sem."
                , {}
            )

            # return invalid model with validation
            ui_view = viewmodel.view(mock_post).content

            self.assertEqual(23, ui_view["content"]["data"]["scheme_of_work_id"])
            self.assertEqual(67, ui_view["content"]["data"]["content_id"])
            self.assertEqual({'display_name': '', 'id': 12, 'published_state': 'published'}, ui_view["content"]["active_model"])
            self.assertFalse(ui_view["content"]["data"]["model"].is_valid)
            self.assertEqual({'letter_prefix': 'aB is not valid. value must be an uppercase letter'}, ui_view["content"]["validation_errors"])
            #self.assertEqual("errors", ui_view["session"]["alert_message"])

