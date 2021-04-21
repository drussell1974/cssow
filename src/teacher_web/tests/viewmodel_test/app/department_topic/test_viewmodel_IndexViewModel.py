from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.department_topic.viewmodels import DepartmentTopicIndexViewModel as ViewModel
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_topic import TopicModel as Model
from shared.models.cls_year import YearModel 
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_IndexViewModel(TestCase):

    def fake_topic_model(self, id, name, auth_ctx):
        
        ''' create top level topic '''
        fake_model_top = Model(1, "Top level topic", lvl=0, auth_ctx=auth_ctx)
        
        ''' create level 1 topic '''
        fake_model_prt = Model(id, name, lvl=1, auth_ctx=auth_ctx)
        fake_model_prt.parent_id = fake_model_top.id
        fake_model_prt.parent = fake_model_top

        # arrange
        
        fake_model1 = Model(12345, "sub topic 1", lvl=2, auth_ctx=auth_ctx)
        fake_model1.parent_id = fake_model_prt.id
        fake_model1.parent = fake_model_prt

        fake_model1 = Model(12346, "sub topic 1", lvl=2, auth_ctx=auth_ctx)
        fake_model1.parent_id = fake_model_prt.id
        fake_model1.parent = fake_model_prt

        return fake_model_prt


    def setUp(self):
        pass


    def tearDown(self):
        pass


    @patch.object(DepartmentContextModel, "get_context_model", return_value=DepartmentContextModel(id_=34, name="Tumbing Dice - Rolling Stones", topic_id=3, is_from_db=True))
    def test_init_called_fetch__no_return_rows(self, DepartmentCtxModel_get_model, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, auth_ctx=mock_auth_user)
            # assert functions was called
            Model.get_all.assert_called()

            self.assertEqual(0, len(actual_result.model))


    @patch.object(DepartmentContextModel, "get_context_model", return_value=DepartmentContextModel(id_=34, name="Tumbing Dice - Rolling Stones", topic_id=3, is_from_db=True))
    def test_init_called_fetch__single_item(self, DepartmentCtxModel_get_model, mock_auth_user):
        
        # arrange
        
        fake_model = self.fake_topic_model(34, "Parent 1", mock_auth_user)

        
        data_to_return = [fake_model]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, auth_ctx=mock_auth_user)
            #actual_result.view()

            # assert
            Model.get_all.assert_called()

            self.assertEqual(1, len(actual_result.model))
            

    @patch.object(DepartmentContextModel, "get_context_model", return_value=DepartmentContextModel(id_=34, name="Tumbing Dice - Rolling Stones", topic_id=3, is_from_db=True))
    def test_init_called_fetch__multiple_items(self, DepartmentCtxModel_get_model, mock_auth_user):
        

        # arrange
        
        fake_model1 = self.fake_topic_model(91, "Tic", mock_auth_user)
                
        fake_model2 = self.fake_topic_model(92, "Tac", mock_auth_user)
        
        fake_model3 = self.fake_topic_model(93, "Tac", mock_auth_user)
        
        
        data_to_return = [fake_model1, fake_model2, fake_model3]
        
        # act

        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, auth_ctx=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
