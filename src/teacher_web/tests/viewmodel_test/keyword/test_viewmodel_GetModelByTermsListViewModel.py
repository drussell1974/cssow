from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from shared.viewmodels.keyword_viewmodels import KeywordGetModelByTermsViewModel as ViewModel
from shared.models.cls_keyword import KeywordDataAccess as DataAccess, KeywordModel as Model


class test_viewmodel_KeywordGetModelByTermsViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_fetch__with_exception(self):
        
        # arrange
        
        with patch.object(DataAccess, "get_by_terms", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            with self.assertRaises(KeyError):
                # act and assert
                ViewModel(db, 22, allow_all=True, auth_user=99)



    def test_init_called_fetch__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(DataAccess, "get_by_terms", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            result = ViewModel(db, 22, allow_all=True, auth_user=99)

            # assert functions was called
            DataAccess.get_by_terms.assert_called()
            self.assertIsNone(result.model)


    def test_init_called_fetch__return_item(self):
        
        # arrange
        
        data_to_return = Model(101)
        
        with patch.object(DataAccess, "get_by_terms", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            result = ViewModel(db, 23, allow_all=True, auth_user=99)

            # assert functions was called
            DataAccess.get_by_terms.assert_called()
            self.assertEqual(101, result.model.id)


    def test_init_called_fetch__return_multiple_items(self):
        
        # arrange
        
        with patch.object(DataAccess, "get_by_terms", return_value=Model(101)):

            db = MagicMock()
            db.cursor = MagicMock()

            # act
            result = ViewModel(db, "DIMM", allow_all=True, auth_user=99)

            # assert functions was called
            DataAccess.get_by_terms.assert_called()
            self.assertEqual(101, result.model.id)