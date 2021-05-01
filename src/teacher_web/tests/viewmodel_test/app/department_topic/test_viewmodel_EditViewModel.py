from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.ks123pathways.viewmodels import KS123PathwayEditViewModel as ViewModel
from shared.models.cls_department import DepartmentModel 
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
from shared.models.cls_topic import TopicModel
from shared.models.utils.breadcrumb_generator import BreadcrumbGenerator
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(BreadcrumbGenerator, "get_items", return_value=fake_breadcrumbs())
class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_view_when_new(self, mock_auth_user, mock_bc):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        topic_options_to_return = [TopicModel(67, "Algorithms", auth_ctx=mock_auth_user), TopicModel(68, "Hardware", auth_ctx=mock_auth_user)]        

        return_pathway_model = Model(101, objective="Integer pretium ultrices dolor, eget convallus purus, volutpat finibus turpis tempus in.", ctx=None)
        return_pathway_model.is_valid = True

        with patch.object(Model, "get_model", return_value=return_pathway_model):
            with patch.object(TopicModel, "get_options", return_value=topic_options_to_return):

                # act

                test_context = ViewModel(db=mock_db, request=mock_request, auth_ctx=mock_auth_user, pathway_item_id = 0)
                
                test_context.view(mock_request)
                
                # assert 

                TopicModel.get_options.assert_called()

                self.assertEqual("", test_context.error_message)
                self.assertFalse(test_context.saved)
                
                Model.get_model.assert_not_called()

                # returns new model
                self.assertEqual(0, test_context.model.id)
                self.assertEqual("", test_context.model.objective)


    def test_view_when_existing(self, mock_auth_user, mock_bc):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "GET"
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        topic_options_to_return = [TopicModel(67, "Algorithms", auth_ctx=mock_auth_user), TopicModel(68, "Hardware", auth_ctx=mock_auth_user)]        

        return_pathway_model = Model(101, objective="Integer pretium ultrices dolor, eget convallus purus, volutpat finibus turpis tempus in.", ctx=None)
        return_pathway_model.is_valid = True

        with patch.object(Model, "get_model", return_value=return_pathway_model):
            with patch.object(TopicModel, "get_options", return_value=topic_options_to_return):

                # act

                test_context = ViewModel(db=mock_db, request=mock_request, auth_ctx=mock_auth_user, pathway_item_id = 101)
                
                test_context.view(mock_request)
                
                # assert 

                TopicModel.get_options.assert_called()

                self.assertEqual("", test_context.error_message)
                self.assertFalse(test_context.saved)
                
                Model.get_model.assert_called()

                # fetch the model
                self.assertEqual(101, test_context.model.id)
                self.assertEqual("Integer pretium ultrices dolor, eget convallus purus, volutpat finibus turpis tempus in.", test_context.model.objective)


    def test_execute_called_save_when_valid(self, mock_auth_user, mock_bc):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "objective": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "year_id": 7,
                    "topic_id": 4,
                    "published": "PUBLISH",
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        on_save__data_to_return = Model(99, objective="Proin id massa metus. Aliqua tincidunt.", ctx=None)
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(db=mock_db, request=mock_request, auth_ctx=mock_auth_user)
            
            test_context.execute()
            
            # assert 

            self.assertEqual("", test_context.error_message)
            self.assertTrue(test_context.saved)
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.objective)

    
    def test_execute_called_save__return_when_invalid(self, mock_auth_user, mock_bc):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 101,
                    "objective": "",
                    "year_id": 7,
                    "topic_id": 4,
                    "published": "PUBLISH",
                }

        return_pathway_model = Model(101, objective="Integer pretium ultrices dolor, eget convallus purus, volutpat finibus turpis tempus in.", ctx=mock_auth_user)
        return_pathway_model.is_valid = True

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        with patch.object(Model, "get_model", return_value=return_pathway_model):
            with patch.object(Model, "save", return_value=None):
                    
                # act
                
                test_context = ViewModel(db=mock_db, request=mock_request, auth_ctx=mock_auth_user, pathway_item_id=99)
                
                test_context.execute()

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'objective': 'required'}", test_context.alert_message)
                self.assertFalse(test_context.saved)

                Model.save.assert_not_called()

                # return the invalid object
                self.assertEqual(101, test_context.model.id)
                self.assertEqual("", test_context.model.objective)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
