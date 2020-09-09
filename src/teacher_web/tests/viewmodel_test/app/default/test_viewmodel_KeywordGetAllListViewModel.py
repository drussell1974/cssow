from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import KeywordGetAllListViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model

@skip("Verify usage")
class test_viewmodel_KeywordGetAllListViewModel(TestCase):

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

            # act
            actual_result = ViewModel(db, 34, 6079)
            # assert functions was called
            Model.get_all.assert_called()
            self.assertEqual(0, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34, "")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db, 38)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(1, len(actual_result.model))
            


    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(91, "Tic"), Model(92, "Tac"), Model(93, "Toe")]
        
        with patch.object(Model, "get_all", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db, 92, 6079)

            # assert functions was called
            Model.get_all.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            