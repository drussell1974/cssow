from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.ks123pathways.viewmodels import KS123PathwayIndexViewModel as ViewModel
from shared.models.cls_ks123pathway import KS123PathwayModel as Model
from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_topic import TopicModel
from shared.models.cls_year import YearModel 
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_IndexViewModel(TestCase):

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

            self.assertEqual(0, len(actual_result.model()))


    @patch.object(DepartmentContextModel, "get_context_model", return_value=DepartmentContextModel(id_=34, name="Tumbing Dice - Rolling Stones", topic_id=3, is_from_db=True))
    def test_init_called_fetch__single_item(self, DepartmentCtxModel_get_model, mock_auth_user):
        
        # arrange
        fake_model = Model(34, "", year_id=7, topic_id=3, ctx=None)
        fake_model.topic = TopicModel(3, "Hardware", auth_ctx=mock_auth_user)
        fake_model.year = YearModel(13, "Year 13")
 
 
        data_to_return = [fake_model]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, auth_ctx=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()

            self.assertEqual(1, len(actual_result.model()))
            

    @patch.object(DepartmentContextModel, "get_context_model", return_value=DepartmentContextModel(id_=34, name="Tumbing Dice - Rolling Stones", topic_id=3, is_from_db=True))
    def test_init_called_fetch__multiple_items(self, DepartmentCtxModel_get_model, mock_auth_user):
        
        # arrange
        
        fake_model1 = Model(91, "Tic", year_id=7, topic_id=3, ctx=mock_auth_user)
        fake_model1.topic = TopicModel(3, "Hardware", auth_ctx=mock_auth_user)
        fake_model1.year = YearModel(7, "Year 7")

        fake_model2 = Model(92, "Tac", year_id=7, topic_id=3, ctx=mock_auth_user)
        fake_model2.topic = TopicModel(1, "Algorithms", auth_ctx=mock_auth_user)
        fake_model2.year = YearModel(7, "Year 7")

        fake_model3 = Model(93, "Toe", year_id=8, topic_id=3, ctx=mock_auth_user)
        fake_model3.topic = TopicModel(3, "Hardware", auth_ctx=mock_auth_user)
        fake_model3.year = YearModel(8, "Year 8")

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
            
            self.assertEqual(2, len(actual_result.model()))
