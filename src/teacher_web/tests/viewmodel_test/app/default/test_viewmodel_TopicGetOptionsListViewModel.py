from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.default.viewmodels import TopicGetOptionsListViewModel as ViewModel
from shared.models.cls_topic import TopicDataAccess as DataAccess, TopicModel as Model

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_TopicGetOptionsListViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = []
        
        with patch.object(DataAccess, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db, topic_id=1)

            # assert functions was called
            DataAccess.get_options.assert_called()
            self.assertEqual(0, len(actual_result.model))
            

    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(34, "")]
        
        with patch.object(DataAccess, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db)

            # assert functions was called
            DataAccess.get_options.assert_called()
            
            self.assertEqual(1, len(actual_result.model))
            


    def test_init_called_fetch__single_item(self):
        
        # arrange
        
        data_to_return = [Model(181, "Tic"), Model(182, "Tac"), Model(183, "Toe")]
        
        with patch.object(DataAccess, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db, topic_id=5)

            # assert functions was called
            DataAccess.get_options.assert_called()
            
            self.assertEqual(3, len(actual_result.model))
            