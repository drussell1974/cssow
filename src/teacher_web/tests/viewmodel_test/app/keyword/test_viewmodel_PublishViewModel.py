import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.keywords.viewmodels import KeywordPublishModelViewModel as ViewModel
from shared.models.cls_keyword import KeywordModel as Model

class test_viewmodel_PublishViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    
    def test_init_called_publish__with_exception(self):
        
        # arrange        
        with patch.object(Model, "publish_by_id", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, keyword_id=101, auth_user=99)


    
    def test_init_called_publish__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "publish_by_id", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, keyword_id=13, auth_user=99)

            # assert functions was called
            Model.publish_by_id.assert_called()
            self.assertIsNone(self.viewmodel.model)


    
    def test_init_called_publish__return_item(self):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = 1

        
        with patch.object(Model, "publish_by_id", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, keyword_id=13, auth_user=99)

            # assert functions was called
            Model.publish_by_id.assert_called()
            self.assertEqual(912, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.term)
            self.assertEqual(1, self.viewmodel.model.published)
