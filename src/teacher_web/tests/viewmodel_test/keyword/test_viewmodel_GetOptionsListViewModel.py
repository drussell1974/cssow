from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from shared.viewmodels.keyword_viewmodels import KeywordGetOptionsListViewModel as ViewModel
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel as Model

#Serializer = test_context.KeywordModelSerializer

class test_viewmodel_KeywordsGetOptionsListViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        expected_result = []
        data_to_return = []
        
        with patch.object(DataAccess, "get_options", return_value=data_to_return):
            
            db = MagicMock()
            db.cursor = MagicMock()

            # act
            actual_result = ViewModel(db)

            # assert functions was called
            DataAccess.get_options.assert_called()
            self.assertEqual(expected_result, actual_result.data)
