from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from shared.viewmodels.keyword_viewmodels import KeywordGetModelViewModel as ViewModel
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel as Model


class test_viewmodel_KeywordGetModelViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(DataAccess, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 22, auth_user=99)

            # assert functions was called
            DataAccess.get_model.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(101, "Abstraction")
        
        with patch.object(DataAccess, "get_model", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            self.viewmodel = ViewModel(db, 23, auth_user=99)

            # assert functions was called
            DataAccess.get_model.assert_called()
            self.assertEqual(101, self.viewmodel.model.id)
            self.assertEqual("Abstraction", self.viewmodel.model.term)
            
