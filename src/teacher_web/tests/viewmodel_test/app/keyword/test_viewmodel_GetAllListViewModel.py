from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch
from app.keywords.viewmodels import KeywordGetAllListViewModel as ViewModel
from shared.models.cls_department import DepartmentModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_teacher import TeacherModel
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_viewmodel_KeywordsGetAllListViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self, mock_auth_user):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(34)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(1, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self, mock_auth_user):
        
        # arrange
        
        data_to_return = [Model(34), Model(35), Model(36)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=mock_auth_user)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(3, len(actual_result.model))            
