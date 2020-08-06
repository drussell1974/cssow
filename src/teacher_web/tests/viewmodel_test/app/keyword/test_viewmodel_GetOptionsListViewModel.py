from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import KeywordGetOptionsListViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_KeywordsGetOptionsListViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(Model, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(0, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34)]
        
        with patch.object(Model, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            
            self.assertEqual(1, len(actual_result.model))
            


    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34), Model(35), Model(36)]
        
        with patch.object(Model, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            