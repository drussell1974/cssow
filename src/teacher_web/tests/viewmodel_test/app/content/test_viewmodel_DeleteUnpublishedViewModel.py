import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.content.viewmodels import ContentDeleteUnpublishedViewModel as ViewModel
from shared.models.cls_content import ContentModel as Model
from shared.models.enums.publlished import STATE

class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exception(self):
        
        # arrange        
        with patch.object(Model, "delete_unpublished", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db=db, auth_user=99, scheme_of_work_id=999)


    def test_init_called_delete__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99, scheme_of_work_id=101)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_delete__return_item(self):
        
        # arrange
        
        data_to_return = [Model(912, "Maecenas sed urna magna", published=STATE.DELETE)]

        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99, scheme_of_work_id=912)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertEqual(912, self.viewmodel.model[0].id)
            self.assertEqual("Maecenas sed urna magna", self.viewmodel.model[0].description)
            self.assertEqual(2, self.viewmodel.model[0].published)


    def test_init_called_delete__return_items(self):
        
        # arrange
        
        data_to_return = [
            Model(312, "Praesent blandit est ut vestibulum", published=STATE.DELETE),
            Model(413, "Ut congue mattis nibh sit", published=STATE.DELETE),
            Model(414, "Donec bibendum mi vitae felis", published=STATE.DELETE)
        ]

        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99, scheme_of_work_id=912)

            # assert functions was called
            Model.delete_unpublished.assert_called()
            self.assertEqual(312, self.viewmodel.model[0].id)
            self.assertEqual("Praesent blandit est ut vestibulum", self.viewmodel.model[0].description)
            self.assertEqual(2, self.viewmodel.model[0].published)

            self.assertEqual(414, self.viewmodel.model[2].id)
            self.assertEqual("Donec bibendum mi vitae felis", self.viewmodel.model[2].description)
            self.assertEqual(2, self.viewmodel.model[2].published)
