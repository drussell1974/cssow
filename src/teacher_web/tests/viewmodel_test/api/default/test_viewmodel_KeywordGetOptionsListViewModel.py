from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from api.default.viewmodels import KeywordGetOptionsListViewModel as ViewModel

from shared.models.cls_keyword import KeywordModel as Model


class test_viewmodel_TopicGetOptionsListViewModel(TestCase):

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

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(0, len(self.viewmodel.model))


    def test_init_called_fetch__single_row(self):
        
        # arrange
        
        data_to_return = [Model(56, term="Nullam")]
        
        with patch.object(Model, "get_options", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(1, len(self.viewmodel.model))


    def test_init_called_fetch__multiple_rows(self):
        
        # arrange
        
        data_to_return = [Model(56, term="placerat"),Model(57, term="Aenean"),Model(58, term="Praesent")]
        
        with patch.object(Model, "get_options", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db)

            # assert functions was called
            Model.get_options.assert_called()
            self.assertEqual(3, len(self.viewmodel.model))