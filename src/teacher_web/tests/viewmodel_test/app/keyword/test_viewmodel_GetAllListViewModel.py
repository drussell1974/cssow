from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.keywords.viewmodels import KeywordGetAllListViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.cls_teacher_permission import TeacherPermissionModel


class test_viewmodel_KeywordsGetAllListViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=6079)

            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=6079)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(1, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34), Model(35), Model(36)]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            mock_request = Mock()

            # act
            actual_result = ViewModel(db=db, request=mock_request, scheme_of_work_id=12, auth_user=6079)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(3, len(actual_result.model))            
